(function ($) {

    var fields_for_types = {
        'ALL': {'translated': ['text', 'image_caption'], 'not-translated': ['image', 'image_position', 'image_width', 'position']},
        'TEXT': {'translated': ['text'], 'not-translated': ['position']},
        'TEXT_W_IMAGE': {'translated': ['text', 'image_caption'], 'not-translated': ['image','image_position', 'image_width', 'position']},
        'TEXT_W_BGIMAGE' : {'translated': ['text'], 'not-translated': ['image', 'position']}
    };

    var hideTypeDependFields = function(parent , type) {
        var first_language = localStorage.getItem('lu.kreios.minimax.language');
        var second_language = localStorage.getItem('lu.kreios.minimax.secondary_language');

        // Hide all fields first
        fields_for_types['ALL']['translated'].forEach(function(class_name) {
            parent.children("."+class_name+"_"+first_language).hide();
            parent.children("."+class_name+"_"+second_language).hide();
        }.bind(parent));

        fields_for_types['ALL']['not-translated'].forEach(function(class_name) {
            parent.children("."+class_name).hide();
        }.bind(parent));

        // Hide not necessary fields
        fields_for_types[type]['translated'].forEach(function(class_name) {
            parent.children("."+class_name+"_"+first_language).show();
            parent.children("."+class_name+"_"+second_language).show();
        }.bind(parent));

        fields_for_types[type]['not-translated'].forEach(function(class_name) {
            parent.children("."+class_name).show();
        }.bind(parent));
    };

    // Keep this on "load" to make sure this runs after the language selector
    $(window).load(function () {
        $(".page-content").each(function() {
            var type_selector = $(this).find("[id$='-type']");
            if (type_selector) {
                hideTypeDependFields(type_selector.parent().parent().parent().parent(), type_selector.val());
            }
        });

        $("[id$='-type']").on("change", function() {
            hideTypeDependFields($(this).parent().parent().parent().parent(), $(this).val());
        })
    });
})(grp.jQuery);
