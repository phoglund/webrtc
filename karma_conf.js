module.exports = function(config) {
  config.set({
    frameworks: ['closure'],
    files: [
      // closure base
      'lib/goog/base.js',

      // included files - tests
      'samples/web/content/**/*.js',

      // source files - these are only watched and served
      {pattern: 'samples/web/content/**/*.js', included: false},

      // external deps
      {pattern: 'lib/goog/deps.js', included: false, served: false}
    ],

    preprocessors: {
      // tests are preprocessed for dependencies (closure) and for iits
      'samples/web/content/**/*.js': ['closure', 'closure-iit'],
      // source files are preprocessed for dependencies
      'samples/web/content/**/*.js': ['closure'],
      // external deps
      'lib/goog/deps.js': ['closure-deps']
    }
  });
};
