(function ($) {
    $.fn.hide_by_type = function(options) {
        // Default target
        var _target = this;

        // Settings
        var $set = $.extend({
            target: _target, // Select input selector
            options: {}      // Select input value => value{ (show|hide):[selector,selector] }
        }, options);

        // If no target input
        if ( !$set.target.length ) {
            throw Error('No select input selected in options target');
        }

        /**
         * Hide/Show related fields | blocks
         * @param $o Options
         * @param $v Input Value
         */
        var toggle = function($o, $v) {
            if ( !$o.hasOwnProperty($v) ) {
                throw Error('Has no option ' + $v + ' defined');
            }

            var opts = $o[$v];
            $(opts.hide.join(', ')).hide();
            $(opts.show.join(', ')).show();
        };

        // Event listener for input
        $($set.target).on('change', function(e){
            toggle($set.options, $(this).val());
        });

        // Triggering event on load
        $($set.target).trigger('change');

        return $set.target;
    };

    $(function(){
        // Technology relation type
        $('#id_technology_relation_type').hide_by_type({
            options: {
                A: {
                    show: [],
                    hide: ['.related_technology_types', '.related_technologies']
                },
                T: {
                    show: ['.related_technology_types'],
                    hide: ['.related_technologies']
                },
                I: {
                    show: ['.related_technologies'],
                    hide: ['.related_technology_types']
                }
            }
        });

        // Solution relation type
        $('#id_solution_relation_type').hide_by_type({
            options: {
                A: {
                    show: [],
                    hide: ['.related_solution_types', '.related_solutions']
                },
                T: {
                    show: ['.related_solution_types'],
                    hide: ['.related_solutions']
                },
                I: {
                    show: ['.related_solutions'],
                    hide: ['.related_solution_types']
                }
            }
        });
    });
})(grp.jQuery);
