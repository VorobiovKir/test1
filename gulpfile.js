(function() {
    'use strict';
    var gulp = require('gulp');
    var sourceMaps = require('gulp-sourcemaps');
    var jshint = require('gulp-jshint');
    var stylish = require('jshint-stylish');
    var jscs = require('gulp-jscs');
    var less = require('gulp-less');
    var sass = require('gulp-sass');
    var concat = require('gulp-concat');
    var copy = require('gulp-copy');
    var rename = require('gulp-rename');
    var flatten = require('gulp-flatten');
    var autoPrefixer = require('gulp-autoprefixer');
    var browserSync = require('browser-sync').create();
    var preprocess = require('gulp-preprocess');
    var rimraf = require('rimraf');

    var paths = {
        // Sources
        css_files: './minimax/static/frontend/less/main.less',
        js_files: './minimax/static/frontend/js/main.js',

        // Watch files
        css_watch_files: './frontend/**/*.less',

        // Targets
        css_target: './minimax/static/frontend/css',
        js_target: './minimax/static/frontend/js',

        // JavaScript plugins
        css_plugin_files: [
            './bower_components/featherlight/release/featherlight.min.css',
        ],

        // JavaScript plugins
        js_plugin_files: [
            './bower_components/jquery/dist/jquery.min.js',
            './bower_components/matchHeight/jquery.matchHeight-min.js',
            './bower_components/smooth-scroll/dist/js/smooth-scroll.min.js',
            './bower_components/bootstrap/js/tooltip.js',
            './bower_components/bootstrap/js/tab.js',
            './bower_components/bootstrap/js/carousel.js',
            './bower_components/bootstrap/js/transition.js',
            './bower_components/featherlight/release/featherlight.min.js',
        ]
    };

    function startWatchers() {
        gulp.watch(paths.css_watch_files, {interval: 500}, ['less']);
        gulp.watch(paths.js_files, {interval: 500}, ['js']);
    }

    gulp.task('clean', function(cb) {
        rimraf('./dist', cb);
    });

    gulp.task('less', function() {
        return gulp.src([].concat(paths.css_plugin_files).concat(paths.css_files))
            .pipe(sourceMaps.init())
            .pipe(less())
            .pipe(autoPrefixer())
            .pipe(concat('app.css'))
            .pipe(sourceMaps.write('.'))
            .pipe(gulp.dest(paths.css_target))
            .pipe(browserSync.stream({once: true}));
    });

    gulp.task('js', function() {
        return gulp.src([].concat(paths.js_plugin_files).concat(paths.js_files))
            .pipe(sourceMaps.init())
            .pipe(concat('app.js'))
            .pipe(sourceMaps.write('.'))
            .pipe(gulp.dest(paths.js_target))
            .pipe(browserSync.stream({once: true}));
    });

    gulp.task('jshint', function() {
        return gulp.src([].concat(paths.js_files,['gulpfile.js']))
            .pipe(jshint())
            .pipe(jshint.reporter(stylish));
    });

    gulp.task('jscs', function() {
        return gulp.src([].concat(paths.js_files,['gulpfile.js']))
            .pipe(jscs());
    });

    gulp.task('assets', ['less', 'js']);

    gulp.task('watch', function() {
        startWatchers();
    });

    gulp.task('live-reload', ['assets'], function() {
        startWatchers();
        browserSync.init({
            proxy: "localhost:8000"
        });
    });

    gulp.task('reload-browser', function() {
        browserSync.reload();
    });

    gulp.task('default', ['assets', 'jshint', 'jscs']);

}());
