//
// EDITOR CONFIGURATION
//

var TINYMCE_CONFIG = {

    // Enable spellchecker on Firefox/Chrome
    browser_spellcheck: true,

    // Disable file uploads
    automatic_uploads: false,

    // Any new paragraph created by e.g. pressing "Enter" should not inherit its styles from
    // the one you happen to have currently selected
    keep_styles: false,

    // Force TinyMCE to use English translations when drawing its UI
    // TODO: Make this inherit the language code form our Django session, instead
     language: 'en',

    // Prevent the user from manually resizing tables or images
    object_resizing: false,

    // Do not show the menu bar.
    menubar: false,

    // The list of plug-ins to enable for this editor
    plugins: 'autoresize,fullscreen,link,paste,wordcount,searchreplace,tabfocus,contextmenu',

    // The additional margin to be shown at the end of the RTE
    autoresize_bottom_margin: 10,

    //
    toolbar: ',undo,redo,|,styleselect,|,bold,italic,underline,|,bullist,numlist,|,fullscreen,link,paste,searchreplace,table',

    // The list of available block and inline styles the user can select from
    style_formats : [
        {title : 'H1', block : 'h1'},
        {title : 'H2', block : 'h2'},
        {title : 'H3', block : 'h3'},
        {title : 'H4', block : 'h4'},
        {title : 'H5', block : 'h5'},
        {title : 'H6', block : 'h6'},
        {title : 'lead', block : 'p', classes: 'lead'},
        {title : 'small', block : 'p', classes: 'small'}
    ],

    // Hide the status
    statusbar: false,

    // This option enables or disables the element cleanup functionality
    verify_html: true,

    // Try to fix broken nested lists
    fix_list_elements: true,

    // All characters will be stored in non-entity form except &amp; &lt; &gt; and &quot;
    entity_encoding : "raw",

    // Styles for editor content
    content_css: "/static/minimax/css/richtext_editor_content.css",

    // What HTML elements should be preserved, e.g. during copy & paste
    valid_elements : ''
    + "h1,h2,h3,h4,h5,h6"
    + "ol,ul,li,"
    + "p[class],span[style],"
    + "strong/b,em,"
    + "br,"
    + "div[class],"
    + "table,td[colspan],tr,tbody,"
    + "a[href|target]"
};

//
// INITIALIZATION/INTEGRATION
//

(function ($) {

    $(document).ready(function () {
        $('.vRichTextField').each(function(){
            // Ignore everything that appears within one of the templates
            // Grappelli uses for creating new inline forms at run-time
            if ($(this).parents('.grp-empty-form').length === 0 && $(this).parents('.grp-closed').length === 0) {
                var additional_config = {
                    mode: 'exact',
                    elements: this.id
                };
                var updated_tiny_mce_config = $.extend({},TINYMCE_CONFIG,additional_config);
                tinyMCE.init(updated_tiny_mce_config);
            }
        });
    });

    // Since we don't wanna copy & modify the actual stacked.html template from Grappelli itself,
    // let's hook into the guts of the Grappelli "inline" jQuery plugin to detect when a new
    // inline gets added (so we can check for any new rich-text fields it may contain)
    // (HACK: Depends on order in which JavaScript files are registered in host page!)
    var original_grp_inline = $.fn.grp_inline;
    $.fn.grp_inline = function (options) {
        var original_onAfterAdded = options.onAfterAdded;
        options.onAfterAdded = function(form) {
            original_onAfterAdded.apply(this, arguments);
            form.find('.vRichTextField').each(function(){
                var additional_config = {
                    mode: 'exact',
                    elements: this.id
                };
                var updated_tiny_mce_config = $.extend({},TINYMCE_CONFIG,additional_config);
                tinyMCE.init(updated_tiny_mce_config);
            });
            form.prop('initialized-editors', 'true');
        };
        return original_grp_inline.apply(this, arguments);
    };

    // Same for collapsible inlines: We should make sure that initialization of richtext boxes
    // within those gets delayed till the moment their opened by the user
    var original_grp_collapsible = $.fn.grp_collapsible;
    $.fn.grp_collapsible = function (options) {
        if (!options) {
            options = {}
        }
        $(this).filter(".grp-closed").not('.grp-empty-form').not('.grp-stacked').prop('initialized-editors', 'false');
        $(this).filter(".grp-closed .grp-closed").not('.grp-empty-form').prop('initialized-editors', 'false');
        options['on_toggle'] = function(elem, options) {
            if ($(elem).prop('initialized-editors') === 'false') {
                elem.find('.vRichTextField').each(function(el){
                    var additional_config = {
                        mode: 'exact',
                        elements: this.id
                    };
                    var updated_tiny_mce_config = $.extend({},TINYMCE_CONFIG,additional_config);
                    tinyMCE.init(updated_tiny_mce_config);
                });
                elem.find('.vRichTextFieldWithTables').each(function(){
                    tinyMCE.init($.extend({}, TINYMCE_WITH_TABLES_CONFIG, {
                        mode: 'exact',
                        elements: this.id
                    }));
                });
                $(elem).prop('initialized-editors', 'true');
            }
        };
        return original_grp_collapsible.apply(this, [ options ]);
    }
})(grp.jQuery);
