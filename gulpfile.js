var gulp = require('gulp'),
  cleanCSS = require('gulp-clean-css'),
  concat = require('gulp-concat'),
  plumber = require('gulp-plumber'),
  uglify = require('gulp-uglify');


var assets = {
  favicon: 'assets/favicon.ico',
  fonts: [
    'node_modules/bootstrap/dist/fonts/*',
  ],
  css: [
    'node_modules/bootstrap/dist/css/bootstrap.css'
  ],
  js: [
    'node_modules/jquery/dist/jquery.js',
    'node_modules/bootstrap/dist/js/bootstrap.js',
  ]
}


gulp.task('copy', function() {
  gulp.src(assets.favicon).pipe(gulp.dest('static'));
  gulp.src(assets.fonts).pipe(gulp.dest('static/fonts'));
});

gulp.task('css', function() {
  return gulp.src(assets.css)
    .pipe(plumber())
    .pipe(concat('style.css'))
    .pipe(cleanCSS())
    .pipe(gulp.dest('static/css'));
});


gulp.task('js', function() {
  return gulp.src(assets.js)
    .pipe(plumber())
    .pipe(concat('script.js'))
    .pipe(uglify())
    .pipe(gulp.dest('static/js'));
});

gulp.task('default', ['copy', 'css', 'js']);
