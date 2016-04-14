var keepNavigationDropped = false;
var onNavigation = false;
var navigationDotPositions = [];

$(document).ready(function() {
    $(window).on('resize', function() {
        // initBoxes();
        autoResizeBoxes();
        alignSlideCaption();
        hideInteractiveMapItems();
        clearTimeout($.data(this, 'resizeTimer'));
        $.data(this, 'resizeTimer', setTimeout(function() {
            positionInteractiveMapItems();
        }, 500));
    });

    $(window).on('scroll', function() {
        showHideNavigationDots();
    });

    initMainNavigation();
    initMainMobileNavigation();

    // $('.match-height').matchHeight({
    //     byRow: false,
    //     property: 'height'
    // });

    $('.row-match-height').matchHeight({
        byRow: true,
        property: 'height'
    });

    // $('.carousel').carousel('cycle');

    smoothScroll.init();

    // Make tabs work correctly
    $('ul.tabs li a').click(function(e) {
        $(this).parents('ul').children('li').removeClass('activated');
        $(this).parent('li').addClass('activated');
    });

    var source = $('.page.page-people-akademie .wrapper-grey .col-md-4');
    var winWidth = $(this).width();
    if(winWidth < 992) {
      source.each(function() {
        $(this).appendTo($(this).parent());
      });
    } else {
      source.each(function() {
        $(this).prependTo($(this).parent());
      });
    }
    $(window).on('resize', function () {
      var winWidth = $(this).width();
      if(winWidth < 992) {
        source.each(function() {
          $(this).appendTo($(this).parent());
        });
      } else {
        source.each(function() {
          $(this).prependTo($(this).parent());
        });
      }
    });

    // initNav();
    // initSubNavs();
    // initMobileNav();
    // initSearchAndLocationNav();
    initBoxes();
    alignSlideCaption();
    initNavigationDots();

    initInteractiveMaps();
});

function showHideNavigationDots() {
    if (($(window).scrollTop() > (0.3 * ($('header.header').outerHeight() + $('.slider').outerHeight()))) && !$('.navigation-dots').is(':visible')) {
        $('.navigation-dots').fadeIn();
    }
    if (($(window).scrollTop() < (0.3 * ($('header.header').outerHeight() + $('.slider').outerHeight()))) && $('.navigation-dots').is(':visible')) {
        $('.navigation-dots').fadeOut();
    }
}

function initNavigationDots() {
    $('.wrapper').not('.hidden').each(function() {
        navigationDotPositions.push({
            y: $(this).offset().top,
            label: $(this).data('label')
        });
    });

    for (var i = 0; i < navigationDotPositions.length; i++) {
        if (navigationDotPositions[i].label === undefined) {
            $('.navigation-dots ul').append('<li><a href="#" data-label="' + navigationDotPositions[i].label + '" data-index="' + i + '"></a></li>');
        } else {
            $('.navigation-dots ul').append('<li><a data-toggle="tooltip" data-trigger="hover" data-placement="left" title="' + navigationDotPositions[i].label + '" href="#" data-label="' + navigationDotPositions[i].label + '" data-index="' + i + '"></a></li>');
        }
    }
    $('[data-toggle="tooltip"]').tooltip();

    // Position dots in the middle/right
    $('.navigation-dots').css({'top': (($(window).height() * 0.5) - $('.navigation-dots').outerHeight() * 0.5) + 'px'});

    $('.navigation-dots ul li a').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: navigationDotPositions[$(this).data("index")].y
        }, 350);
    });

    if (navigationDotPositions.length > 1) {
        $(document).on('scroll', function() {
            var position = $(document).scrollTop();
            var index;

            for (var i = 0; i < navigationDotPositions.length; i++) {
                if (position <= navigationDotPositions[i].y) {
                    index = i;
                    break;
                }
            }

            $('.navigation-dots ul li a')
                .removeClass('active')
                .eq(index)
                .addClass('active');
        });
    }
    $('.navigation-dots').hide();
}

function alignSlideCaption() {
    var slideCaptionHeight = $('.slide-caption').outerHeight();
    var slideHeight = $('.slide-caption').parents('.row').outerHeight();
    var slideCaptionPosition = $('.slide-caption').position().y;

    if (slideCaptionHeight < slideHeight) {
        slideCaptionPosition = (slideHeight - slideCaptionHeight) * 0.5;
        $('.slide-caption').css({'top': slideCaptionPosition + 'px'});
    } else {
        $('.slide-caption').css({'top': '0px'});
    }
}

function autoResizeBoxImage(box) {
    var $boxImage = $(box).children('.box-container-image').first();
    var imageUrl = $boxImage.children('img').first().attr('src');

    $boxImage.css({
        'background-image': 'url(' + imageUrl + ')',
        'height': $(box).height() + 'px'
    });
}
autoResizeBoxes();
function autoResizeBoxes() {
  console.log("Fired");
    var topSize = 0;
    var sizeToAdd = 0;

    // Get biggest column
    $.each($('.boxes-container > div'), function(index, item) {
        if (topSize < $(item).height()) {
            topSize = $(item).height();
        }
    });

    // Update smaller columns to match the biggest one
    $.each($('.boxes-container > div'), function(index, item) {
        if (topSize > $(item).height()) {
            sizeToAdd = (topSize - $(item).height()) / $(item).children().size();
            $.each($(item).children(), function(child_index, child_item) {
                var newSize = $(child_item).height() + sizeToAdd;
                $(child_item).css({'height': newSize + 'px'});
            });
        }
        $.each($(item).children(), function(child_index, child_item) {
            autoResizeBoxImage(child_item);
        });
    });
}

function initBoxes() {
    var windowWidth = $('body').width();
    if (windowWidth > 976) {
        autoResizeBoxes();
    }
}

function initMainNavigation() {
    $('nav.navigation > ul > li').off('mouseenter');
    $('nav.navigation > ul > li').on('mouseenter', dropMainNavigation);
    $('nav.navigation > ul > li').on('click', dropMainNavigation);
    $('nav.navigation > ul > li').on('mousemove', function() {
        onNavigation = true;
    });
    $('nav.navigation > ul').on('mouseleave', pullMainNavigation);

    initLocationSelectNavigation();
    initSearchNavigation();
    initMainSubNavigation();
}

function dropMainNavigation(e) {
    if ((e.type == 'mouseenter') && ($('header.header .logo .search .header-dropdown').is(':visible') || $('header.header .logo .location .header-dropdown').is(':visible'))) {
        return false;
    }
    var mainNavigation = this;

    // Reset subnav
    $('.header-dropdown .right-column .sub-sub-nav').empty();
    $('.header-dropdown').find('li.active').removeClass('active');

    $(mainNavigation).children('.header-dropdown').show();

    var spaceToFill = ($(window).width() - $(this).find('.content-wrapper').outerWidth()) / 2;
    var navWidth = $(this).find('.content-wrapper > .right-column').outerWidth() - $(this).find('.content-wrapper > .right-column .sub-sub-nav').outerWidth() - 25;
    var subNavHeight = $(this).find('.content-wrapper > .right-column').outerHeight();
    if ($(this).find('.content-wrapper > .left-column').outerHeight() > subNavHeight) {
        subNavHeight = $(this).find('.content-wrapper > .left-column').outerHeight();
    }

    $('.background-color-box').css({'width': spaceToFill + 'px'});
    $(this).find('.content-wrapper > .right-column > ul').css({'width': navWidth + 'px'});
    $(this).find('.content-wrapper > .right-column .sub-sub-nav').css({'height': subNavHeight + 'px'});

    $(mainNavigation).children('.header-dropdown').hide();

    if (e.type == 'click') {
        pullAllNavigation();
    }
    if (!keepNavigationDropped) {
        keepNavigationDropped = true;
        $(mainNavigation).children('.header-dropdown').slideDown(200);
    } else {
        $(mainNavigation).parent('ul').children('li').children('.header-dropdown').hide();
        $(mainNavigation).children('.header-dropdown').show();
    }
}

function pullMainNavigation() {
    var mainNavigationWrapper = $('nav.navigation > ul');
    onNavigation = false;

    setTimeout(function() {
        if (onNavigation) {
            keepNavigationDropped = true;
        } else {
            keepNavigationDropped = false;
        }

        if (!keepNavigationDropped) {
            $(mainNavigationWrapper).children('li').children('.header-dropdown').slideUp(150);
            keepNavigationDropped = false;
        }
    }, 500);
}

function initMainSubNavigation() {
    $('.header-dropdown .right-column.sub-nav ul > li').on('mouseenter', function() {
        $(this).parent().children('li').removeClass('active');
        $(this).addClass('active');
        var subSubNav = $(this).children('ul').clone();
        if (subSubNav) {
            $('.header-dropdown .right-column .sub-sub-nav').empty();
            $('.header-dropdown .right-column .sub-sub-nav').append(subSubNav);
        }
    });
}

function initLocationSelectNavigation() {
    var dropDown = null;
    $('header.header .logo .search button').on('click', function() {
        pullAllNavigation();
        dropDown = $(this).parent('.search').children('.header-dropdown');

        if ($(dropDown).is(':visible')) {
            pullAllNavigation();
        } else {
            $(this).addClass('active');
            dropDown.slideDown();
        }
    });
}

function initSearchNavigation() {
    var dropDown = null;
    $('header.header .logo .location button').on('click', function() {
        pullAllNavigation();
        dropDown = $(this).parent('.location').children('.header-dropdown');

        if ($(dropDown).is(':visible')) {
            pullAllNavigation();
        } else {
            $(this).addClass('active');
            dropDown.slideDown();
        }
    });
}

function pullAllNavigation() {
    $('.header-dropdown').slideUp();
    $('header.header .logo button.active').removeClass('active');
}

function initMainMobileNavigation() {
    $('.mobile-navigation-button').off('mouseenter');
    $('.mobile-navigation-button').on('click', dropMaiMobileNavigation);
    // $('.mobile-navigation-button').on('mouseleave', pullMainMobileNavigation);

    $('.mobile-navigation > ul > li > a').on('click', dropMaiMobileSubNavigation);
}

function dropMaiMobileNavigation() {
    var mainMobileNavigation = $('.mobile-navigation');

    if (mainMobileNavigation.is(':visible')) {
        pullMainMobileNavigation(mainMobileNavigation);
    } else {
        mainMobileNavigation.slideDown();
    }
}

function pullMainMobileNavigation(mainMobileNavigation) {
    mainMobileNavigation.slideUp();
}

function dropMaiMobileSubNavigation() {
    var mainMobileSubNavigation = $(this).parent().find('> ul');
    $('.mobile-navigation > ul > li > ul').each(function() {
        if ($(this).is(':visible')) {
            $(this).slideUp();
        }
    });

    $(mainMobileSubNavigation).slideDown(function() {
        $(this).find('> li').on('click', function() {
            $(this).find('ul').toggle('slide');
        });
    });
}

function initInteractiveMaps() {
    $('.interactive-map').each(function() {
        var map = $(this);
        var mapName = $(this).data('map-name');
        var mapItems = $('.map-item[data-for-map=' + mapName + ']');

        mapItems.each(function(index) {
            var mapItem = $(this);
            mapItem.data('map-item-id', index);
            /*jshint multistr: true */
            var mapDotItem = $('<div class="map-item-pin" \
                data-map-position-x="' + mapItem.data('map-position-x') + '" \
                data-map-position-y="' + mapItem.data('map-position-y') + '" \
                data-map-related-item-id="' + index + '" \
                data-toggle="map-item-tooltip" data-placement="top" title="' + mapItem.data('map-title') + '" \
                data-title="' + mapItem.data('map-title') + '"><span class="inner"></span></div>"');

            $('body').prepend(mapDotItem);
            positionInteractiveMapItem(mapDotItem, map);
        });
    });

    setTimeout(positionInteractiveMapItems, 500);
}

function hideInteractiveMapItems() {
    $('.map-item-pin').removeClass('animated').fadeOut().off('click');
}

function positionInteractiveMapItem(mapDotItem, map) {
    var mapPercentPixelWidth = $(map).outerWidth() * 0.01;
    var mapPercentPixelHeight = $(map).outerHeight() * 0.01;

    mapPositions = $(map).offset();

    var mapDotPositions = {
        top: mapPositions.top,
        left: mapPositions.left
    };

    $(mapDotItem).css({
        'top': -30 + (mapDotPositions.top + (mapPercentPixelHeight * mapDotItem.data('map-position-y'))) + 'px',
        'left': -30 + (mapDotPositions.left + (mapPercentPixelWidth * mapDotItem.data('map-position-x'))) + 'px',
    });

    $(mapDotItem).on('click', openMapItem);
}

function positionInteractiveMapItems() {
    $('.map-item-pin').off('click');

    var map = $('.interactive-map');
    $('.map-item-pin').each(function() {
        var mapDotItem = $(this);

        setTimeout(function() {
            positionInteractiveMapItem(mapDotItem, map);
            mapDotItem.show().css({'opacity': 0}).fadeTo(500, 0.9, function() {
                mapDotItem.addClass('animated');
                $('[data-toggle="map-item-tooltip"]').tooltip({
                    template: '<div class="tooltip map-item-tooltip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'
                });
                mapDotItem.on('mouseenter', function() {
                    mapDotItem.removeClass('animated');
                }).on('mouseleave', function() {
                    mapDotItem.addClass('animated');
                });
            });
        }, Math.floor((Math.random() * 1500) + 1));
    });
}

function openMapItem() {
    var mapItem = $(this);
    var mapItemContent = $('[data-map-item-id=' + mapItem.data('map-related-item-id') + ']');
    $('.map-item').each(function() {
        if (mapItem.data('map-related-item-id') == $(this).data('map-item-id')) {
            mapItemContent = $(this).html();
        }
    });

    if (mapItemContent.length > 0) {
        $.featherlight(mapItemContent, {
            openSpeed: 200,
            contentFilters: ['html'],
            afterContent: function() {
                var content = $('.featherlight-inner');
                content.css({'top': (($(window).height() / 2) - (content.outerHeight() / 2)) + 'px'});
            }
        });
    }
}
