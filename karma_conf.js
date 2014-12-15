module.exports = function(config) {
  config.set({
    frameworks: ['closure'],
    files: [
      // closure base
      // TODO(phoglund): not sure how to import stuff the adapter needs
      'closure-library/closure/goog/base.js',

      // closure adapter
      'samples/web/js/karma_adapter.js',

      // included files - tests
      'samples/web/content/apprtc/js/*.js',

      // source files - these are only watched and served
      {pattern: 'samples/web/content/apprtc/js/*.js', included: false},

      // external deps
      {pattern: 'closure-library/closure/goog/deps.js',
       included: false, served: false}
    ],

    preprocessors: {
      // tests are preprocessed for dependencies (closure) and for iits
      'samples/web/content/apprtc/js/*.js': ['closure', 'closure-iit'],
      // source files are preprocessed for dependencies
      'samples/web/content/apprtc/js/*.js': ['closure'],
      // external deps
      'closure-library/closure/goog/deps.js': ['closure-deps']
    }
  });
};
