(function ($) {

    var getLanguages = function (rows_by_name_by_language, default_language) {

        // initialize the list with the default language (will be first)
        var languages = [
            { id: default_language, caption: LANGUAGES[ default_language ] }
        ];

        // add all other languages to the list
        $.each(rows_by_name_by_language, function (language, rows_by_name) {
            if (language != default_language) {
                languages.push({ id: language, caption: LANGUAGES[ language ]});
            }
        });

        return languages;
    }

    var isLanguage = function (languages, lang) {
        for (var i = 0; i < languages.length; ++i) {
            if (languages[i].id === lang) {
                return true;
            }
        }
        return false;
    }

    var getRowsByLanguageByName = function () {

        // Iterate all rows (whether or not they contain a translatable field)
        var rows_by_language = {};

        $('.grp-row, .grp-td').each(function (row_index, row_el) {
            $(row_el).find('.mt').each(function (field_index, field_el) {
                // True to guess the actual language from that field's ID
                var id_components = field_el.id.split('_');
                id_components.shift(); // First segment is always "id"
                lang = id_components.pop(); // Last segment is language
                name = id_components.join('_'); // Remaining parts constitute actual field name

                // Remember this particular row by its language and name
                if (!rows_by_language[lang]) {
                    rows_by_language[lang] = {};
                }

                rows_by_language[lang][name] = row_el;
            });
        });
        return rows_by_language;
    }


    var getInlineColumnsByNameByLanguage = function (languages) {
        // Iterate all inline columns (whether or not they contain a translatable field)
        var columns_by_language = {};
        $('.grp-tabular .grp-table .grp-thead .grp-th').each(function (col_index, col_el) {
            var class_names = col_el.className.split(/\s+/);
            for (var i = 0; i < class_names.length; ++i) {
                var class_name_components = class_names[i].split('-');
                lang = class_name_components.pop(); // Last segment is language
                name = class_name_components.join('-'); // Remaining parts constitute actual field name
                if (isLanguage(languages, lang)) {
                    // Remember this particular field by its language and name
                    if (!columns_by_language[lang]) {
                        columns_by_language[lang] = [];
                    }
                    if (!columns_by_language[lang].indexOf(name) > -1) {
                        columns_by_language[lang].push(name);
                    }
                }
            }
            ;
        });
        return columns_by_language;
    }

    var showOnlyRowsForLanguage = function (rows_by_name_by_language, selected_primary_language, selected_secondary_language) {
        // Store the selected language
        try {
            localStorage.setItem('lu.kreios.minimax.language', selected_primary_language);
            localStorage.setItem('lu.kreios.minimax.secondary_language', selected_secondary_language || '');
        } catch(e) {}

        $.each(rows_by_name_by_language, function (language, rows_by_name) {
            $.each(rows_by_name, function (field_name, el) {
                if (language == selected_primary_language || language == selected_secondary_language) {
                    $(el).show();
                }
                else {
                    $(el).hide();
                }
            });
        });
    }

    var showOnlyInlineColumnsForLanguage = function (inline_columns_by_name_by_language, selected_language) {
        $.each(inline_columns_by_name_by_language, function (language, cols_by_names) {
            $.each(cols_by_names, function (index, col_name) {
                if (language == selected_language) {

                    $('.grp-tabular .grp-table').find('.' + col_name + '-' + language + ', .' + col_name + '_' + language).show();
                }
                else {
                    $('.grp-tabular .grp-table').find('.' + col_name + '-' + language + ', .' + col_name + '_' + language).hide();
                }
            });
        });
    }


    var postProcessFieldLabels = function (rows_by_name_by_language) {
        $.each(rows_by_name_by_language, function (language, rows_by_name) {
            $.each(rows_by_name, function (field_name, el) {
                // Remove language and brackets from field label, as they are already
                // displayed within the actual selector
                var field_label = $(el).find('label')
                if (field_label.html()) {
                    field_label.html(field_label.html().replace(/\ \[.+\]/, ''));
                    field_label.addClass('i18n-field-label')
                    field_label.addClass('i18n-field-label-' + language)
                }
            });
        });
    }

    var postProcessInlineFieldLabels = function (inline_columns_by_name_by_language) {
        $.each(inline_columns_by_name_by_language, function (language, cols_by_names) {
            $.each(cols_by_names, function (index, col_name) {
                // Remove language and brackets from field label, as they are already
                // displayed within the actual selector
                var field_label = $('.grp-tabular .grp-table .grp-thead').find('.grp-th.' + col_name + '-' + language)
                if (field_label.html()) {
                    field_label.html(field_label.html().replace(/\ \[.+\]/, ''));
                    field_label.addClass('i18n-field-label')
                    field_label.addClass('i18n-field-label-' + language)
                }
            });
        });
    }

    var addOptions = function(select, languages) {
        $.each(languages, function (index, language) {
          $('<option value="' + language.id + '">' + language.caption + '</option>')
              .prop('checked', index == 0)
              .appendTo(select);
        });
    }

    $(document).ready(function () {
        if ($('body').hasClass('grp-change-form')) {
            var current_language = localStorage.getItem('lu.kreios.minimax.language') || DEFAULT_LANGUAGE;
            var current_secondary_language = localStorage.getItem('lu.kreios.minimax.secondary_language') || DEFAULT_LANGUAGE;

            var rows_by_name_by_language = getRowsByLanguageByName();
            postProcessFieldLabels(rows_by_name_by_language);
            var languages = getLanguages(rows_by_name_by_language, current_language);
            var secondary_languages = getLanguages(rows_by_name_by_language, current_secondary_language)
            var inline_columns_by_name_by_language = getInlineColumnsByNameByLanguage(languages);
            postProcessInlineFieldLabels(inline_columns_by_name_by_language);
            if (languages.length < 2) return; // Not really applicable, here!

            // Create language switcher
            select_primary = $('<select id="content-language-switcher">');
            select_secondary = $('<select id="content-language-switcher-secondary">');
            select_secondary.prop("disabled", true)
            show_secondary = $('<input type="checkbox" id="content-language-switcher-show-secondary">').prop(
              'checked', !!localStorage.getItem('lu.kreios.minimax.secondary_language'));

            addOptions(select_primary, languages);
            addOptions(select_secondary, secondary_languages);
            $('<li>')
                .append('<label for="content-language-switcher" class="content-language-switcher-label">Switch content language:</label>')
                .append(select_primary)
                .append(show_secondary)
                .append('<label for="content-language-switcher-secondary" class="content-language-switcher-label">Secondary language:<label>')
                .append(select_secondary)
                .prependTo('#grp-page-tools > ul');

            var onChange = function (e) {
                var is_show_secondary = show_secondary.is(":checked");
                showOnlyRowsForLanguage(getRowsByLanguageByName(), select_primary.val(), is_show_secondary ? select_secondary.val() : null);
                showOnlyInlineColumnsForLanguage(getInlineColumnsByNameByLanguage(languages), select_primary.val(), is_show_secondary ? select_secondary.val() : null);
            };

            // Register
            select_primary.change(onChange);
            select_secondary.change(onChange);
            show_secondary.change(function (e) {
                select_secondary.prop("disabled", !$(this).is(":checked"));
                select_secondary.change();
            });

            showOnlyRowsForLanguage(rows_by_name_by_language, current_language, current_secondary_language);
            showOnlyInlineColumnsForLanguage(inline_columns_by_name_by_language, current_language);
            show_secondary.change();
        }
    });
})(grp.jQuery);
