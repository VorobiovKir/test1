function MapChosePosition(input_button, image_input) {
    this.coo_wrapper = input_button.parentNode.parentNode.parentNode.parentNode.parentNode;
    this.coordinates = {
        x: this.coo_wrapper.querySelector('.grp-cell.position_x input'),
        y: this.coo_wrapper.querySelector('.grp-cell.position_y input')
    };

    this.src = document.querySelector(image_input).value;
    this.modal = this.get_modal();

    this.img = null;
}

MapChosePosition.prototype.set = function(coor) {
    for ( var k in coor ) {
        if ( this.coordinates.hasOwnProperty(k) ) {
            this.coordinates[k].value = coor[k];
        }
    }
};

MapChosePosition.prototype.get_modal = function() {
    if ( !this.src ) {
        return;
    }

    var modal_element = document.getElementById('modal-map');
    if ( modal_element ) {
        modal_element.querySelector('img').setAttribute('src', this.src);
        return modal_element;
    }

    var map = this,
        wrapper = document.createElement('div'),
        modal = document.createElement('div'),
        image_wrap = document.createElement('div'),
        image = document.createElement('img'),
        point = document.createElement('div'),
        save = document.createElement('button'),
        cancel = document.createElement('button');

    // Modal wrapper
    wrapper.id = 'modal-map';
    wrapper.className = 'file-map-modal-wrapper';

    // Modal
    modal.className = 'file-map-modal';

    // Image wrapper
    image_wrap.className = 'image-wrap';

    // Point
    point.className = 'image-target-point';

    if (map.coordinates.x.value !== '' && map.coordinates.y.value !== '') {
        point.style.display = 'block';
        point.style.top = map.coordinates.y.value + '%';
        point.style.left = map.coordinates.x.value + '%';
    }

    // Add button
    save.innerHTML = 'Save';
    save.className = 'grp-button file-save';
    save.addEventListener('click', function(e) {
        e.preventDefault();
        map.set({
            x: image.point_x,
            y: image.point_y
        });
        map.modal.remove();
        point.style.display = 'none';
    });

    // Cancel button
    cancel.innerText = 'Cancel';
    cancel.className = 'grp-button btn-cancel grp-delete-link';
    cancel.addEventListener('click', function(e){
        e.preventDefault();
        map.modal.remove();
        point.style.display = 'none';
    });

    // Image
    image.src = this.src;
    image.addEventListener('load', function(){
        image.addEventListener('click', function(e){
            image.point_x = Math.round(e.offsetX / (e.target.clientWidth / 100) * 100) / 100;
            image.point_y = Math.round(e.offsetY / (e.target.clientHeight / 100) * 100) / 100;

            // set Point style
            point.style.top = image.point_y + '%';
            point.style.left = image.point_x + '%';
            point.style.display = 'block';
        })
    });

    image_wrap.appendChild(image);
    image_wrap.appendChild(point);
    modal.appendChild(image_wrap);
    modal.appendChild(cancel);
    modal.appendChild(save);
    wrapper.appendChild(modal);
    document.getElementsByTagName('body')[0].appendChild(wrapper);

    return document.getElementById('modal-map');
};


function getImagePointSelector(element, image) {
    var map = new MapChosePosition(element, image);
};
