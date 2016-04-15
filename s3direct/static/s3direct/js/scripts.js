(function(){

    "use strict";

    var getCookie = function(name) {
        var value = '; ' + document.cookie,
            parts = value.split('; ' + name + '=');
        if (parts.length == 2) return parts.pop().split(';').shift()
    };

    var request = function(method, url, data, headers, el, showProgress, cb) {
        var req = new XMLHttpRequest();
        req.open(method, url, true);

        Object.keys(headers).forEach(function(key){
            req.setRequestHeader(key, headers[key])
        });

        req.onload = function() {
            cb(req.status, req.responseText)
        };

        req.onerror = req.onabort = function() {
            disableSubmit(false);
            error(el, 'Sorry, failed to upload file.')
        };

        req.upload.onprogress = function(data) {
            progressBar(el, data, showProgress)
        };

        req.send(data)
    };

    var parseURL = function(text) {
        var xml = new DOMParser().parseFromString(text, 'text/xml'),
            tag = xml.getElementsByTagName('Location')[0],
            url = unescape(tag.childNodes[0].nodeValue);

        return url
    };

    var parseJson = function(json) {
        var data;
        try {data = JSON.parse(json)}
        catch(e){ data = null }
        return data
    };

    var progressBar = function(el, data, showProgress) {
        if(data.lengthComputable === false || showProgress === false) return;

        var pcnt = Math.round(data.loaded * 100 / data.total),
            bar  = el.querySelector('.bar');

        bar.style.width = pcnt + '%'
    };

    var error = function(el, msg) {
        el.className = 's3direct form-active';
        el.querySelector('.file-input').value = '';
        alert(msg)
    };

    var update = function(el, xml) {
        var thumb_url = el.querySelector('.file-thumb'),
            thumb_img = el.querySelector('.file-thumb img'),
            link = el.querySelector('.file-link'),
            url  = el.querySelector('.file-url');

        url.value = parseURL(xml);
        if ( link ) {
            link.setAttribute('href', url.value);
            link.innerHTML = url.value.split('/').pop();
        }

        if ( thumb_img && thumb_url ) {
            thumb_url.setAttribute('href', url.value);
            thumb_img.setAttribute('src', url.value);
            thumb_img.setAttribute('alt', url.value.split('/').pop());
        }

        el.className = 's3direct link-active';
        el.querySelector('.bar').style.width = '0%';
    };

    var concurrentUploads = 0;
    var disableSubmit = function(status) {
        var submitRow = document.querySelector('.submit-row');
        if( ! submitRow) return;

        var buttons = submitRow.querySelectorAll('input[type=submit]');

        if (status === true) concurrentUploads++;
        else concurrentUploads--

        ;[].forEach.call(buttons, function(el){
            el.disabled = (concurrentUploads !== 0)
        })
    };

    var upload = function(file, data, el, cb) {
        var form = new FormData();

        disableSubmit(true);

        if (data === null) return error(el, 'Sorry, could not get upload URL.');

        el.className = 's3direct progress-active';
        var url  = data['form_action'];
        delete data['form_action'];

        Object.keys(data).forEach(function(key){
            form.append(key, data[key])
        });
        form.append('file', file);

        request('POST', url, form, {}, el, true, function(status, xml){
            disableSubmit(false);
            if(status !== 201) return error(el, 'Sorry, failed to upload to S3.');
            update(el, xml);
            (cb || function(){})(parseURL(xml));
        })
    };

    var getUploadURL = function(e) {
        var el       = e.target.parentElement,
            file     = el.querySelector('.file-input').files[0],
            dest     = el.querySelector('.file-dest').value,
            url      = el.getAttribute('data-policy-url'),
            form     = new FormData(),
            headers  = {'X-CSRFToken': getCookie('csrftoken')};

        form.append('type', file.type);
        form.append('name', file.name);
        form.append('dest', dest);

        request('POST', url, form, headers, el, false, function(status, json){
            var data = parseJson(json);

            switch(status) {
                case 200:
                    upload(file, data, el);
                    break;
                case 400:
                case 403:
                    error(el, data.error);
                    break;
                default:
                    error(el, 'Sorry, could not get upload URL.')
            }
        })
    };

    var showImageEditor = function(e) {
        e.preventDefault();

        var edit = new ImageEditor(e.target);
        edit.init();
    };

    var removeUpload = function(e) {
        e.preventDefault();

        var el = e.target.parentElement;
        el.querySelector('.file-url').value = '';
        el.querySelector('.file-input').value = '';
        el.className = 's3direct form-active'
    };

    var addHandlers = function(el) {
        var url    = el.querySelector('.file-url'),
            input  = el.querySelector('.file-input'),
            remove = el.querySelector('.file-remove'),
            status = (url.value === '') ? 'form' : 'link',
            editor = el.querySelector('.file-edit');

        el.className = 's3direct ' + status + '-active';

        remove.addEventListener('click', removeUpload, false);
        input.addEventListener('change', getUploadURL, false);
        if ( editor ) {
            editor.addEventListener('click', showImageEditor, false);
        }
    };

    document.addEventListener('DOMContentLoaded', function(e) {
        [].forEach.call(document.querySelectorAll('.s3direct'), addHandlers)
    });

    document.addEventListener('DOMNodeInserted', function(e){
        if(e.target.tagName) {
            var el = e.target.querySelector('.s3direct');
            if(el) addHandlers(el)
        }
    });

    /**
     * Edited image form
     *
     * @param target
     * @constructor
     */
    function ImageEditor(target) {
        this.cropper = null;
        this.filename = target.parentNode.querySelector('.file-thumb img').getAttribute('alt');
        this.filepath = target.parentNode.querySelector('.file-thumb img').getAttribute('src');
        this.modal = document.querySelector(target.getAttribute('data-target'));
        this.binds = {};
        this.btn = {
            save: this.modal.querySelector('.file-save'),
            cancel: this.modal.querySelector('.file-cancel')
        };

        var editor = this;

        // Clear cropper wrapper
        this.bindAction('editor.loaded', function(){
            editor.clearWrapper();
            editor.modal.querySelector('img').setAttribute('src', editor.filepath);
            editor.modal.classList.add('active');
        });

        // Initialize cropper
        this.bindAction('image.loaded', function(img){
            // Resize wrapper to image width
            img.parentNode.style.width = (img.clientWidth + 'px');

            // Initialize cropper
            editor.cropper = new Cropper(img, {
                dragMode: 'move'
            });
        });

        // Cancel edition
        this.bindAction('editor.cancel', function(e){
            editor.cropper.destroy();
            editor.clearWrapper();
            editor.modal.classList.remove('active');
        });

        // Zoom
        this.bindAction('editor.zoom_in', function(e){ editor.cropper.zoom(0.1) });
        this.bindAction('editor.zoom_out', function(e){ editor.cropper.zoom(-0.1) });

        // Saving
        this.bindAction('editor.save', function(e){
            editor.upload(target.parentNode);
            editor.callAction('editor.cancel');
        });

        // Image uploaded
        this.bindAction('image.uploaded', function(url){
            target.parentNode.querySelector('.file-thumb').setAttribute('href', url);
            target.parentNode.querySelector('.file-thumb img').setAttribute('href', url);
        });

        // Control events
        this.btn.save.addEventListener('click', function(e){ editor.callAction('editor.save', e) });
        this.btn.cancel.addEventListener('click', function(e){ editor.callAction('editor.cancel', e) });
    }

    /**
     * Bind callback on editor action
     *
     * @param action
     * @param callback
     */
    ImageEditor.prototype.bindAction = function(action, callback) {
        this.binds[action] = callback;
    };

    /**
     * [!HOTFIX Cropper] Clear editor wrapper
     */
    ImageEditor.prototype.clearWrapper = function() {
        this.modal.querySelector('.file-edit-image').innerHTML = '<img src="" />';
    };

    /**
     * Call editor action
     *
     * @param action
     * @param data
     * @returns {*}
     */
    ImageEditor.prototype.callAction = function(action, data) {
        if ( data && data.preventDefault ) data.preventDefault();
        return (this.binds[action] || function(){})(data);
    };

    /**
     * Initialize editor
     */
    ImageEditor.prototype.init = function() {
        // Editor load event
        this.callAction('editor.loaded');

        // Image loaded event
        var editor = this;
        var target_image = this.modal.querySelector('img');
        target_image.addEventListener('load', function(e){
            e.preventDefault();
            editor.callAction('image.loaded', target_image);
        });
    };

    /**
     * Upload image
     *
     * @param el
     */
    ImageEditor.prototype.upload = function(el) {
        var editor   = this,
            file     = this.blob(),
            dest     = el.querySelector('.file-dest').value,
            url      = el.getAttribute('data-policy-url'),
            form     = new FormData(),
            headers  = {'X-CSRFToken': getCookie('csrftoken')};

        form.append('type', this.mime());
        form.append('name', this.filename);
        form.append('dest', dest);

        request('POST', url, form, headers, el, false, function(status, json){
            var data = parseJson(json);

            switch(status) {
                case 200:
                    upload(file, data, el, function(new_url){
                        editor.callAction('image.uploaded', new_url);
                    });
                    break;
                case 400:
                case 403:
                    error(el, data.error);
                    break;
                default:
                    error(el, 'Sorry, could not get upload URL.')
            }
        })
    };

    /**
     * Get DataURL from cropped canvas
     *
     * @returns {string}
     */
    ImageEditor.prototype.dataURL = function() {
        return this.cropper.getCroppedCanvas().toDataURL(this.mime());
    };

    /**
     * Get Image MIME-Type from extension
     *
     * @returns {string}
     */
    ImageEditor.prototype.mime = function() {
        var types = {
            jpg: 'jpeg'
        };

        var ext = this.filename.split('.');
        ext = ext[ext.length - 1].toLowerCase();

        var mime = ext;
        if ( types.hasOwnProperty(mime) ) {
            mime = types[mime];
        }

        return 'image/' + mime;
    };

    /**
     * Make Blob from DataURL
     *
     * @returns {*}
     */
    ImageEditor.prototype.blob = function() {
        var BASE64_MARKER = ';base64,',
            dataURL = this.dataURL();
        if (dataURL.indexOf(BASE64_MARKER) == -1) {
          var parts = dataURL.split(',');
          var contentType = parts[0].split(':')[1];
          var raw = decodeURIComponent(parts[1]);

          return new Blob([raw], {type: contentType});
        }

        var parts = dataURL.split(BASE64_MARKER);
        var contentType = parts[0].split(':')[1];
        var raw = window.atob(parts[1]);
        var rawLength = raw.length;

        var uInt8Array = new Uint8Array(rawLength);

        for (var i = 0; i < rawLength; ++i) {
          uInt8Array[i] = raw.charCodeAt(i);
        }

        return new Blob([uInt8Array], {type: contentType});
    };

})();
