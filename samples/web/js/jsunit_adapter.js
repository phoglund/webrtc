/*
 *  Copyright (c) 2014 The WebRTC project authors. All Rights Reserved.
 *
 *  Use of this source code is governed by a BSD-style license
 *  that can be found in the LICENSE file in the root of the source
 *  tree.
 */

/**
 * This primitive adapter makes it possible to write our tests jsunit-style
 * and still execute them as js-test-driver tests.
 */
(function() {
  function makeTestCaseName() {
    var scripts = document.getElementsByTagName('script');
    var lastScript = scripts[scripts.length-1];
    return lastScript.src;
  }

  var testCaseForFile = new TestCase(makeTestCaseName()); 

  function createTestMethod(name, testFunction) {
    if (typeof testFunction != 'function')
      return;

    testCaseForFile.prototype[name] = testFunction;
  }

  // Find all tests and map to js-test-driver tests.
  for (var propertyName in window) {
    if (propertyName.indexOf('test') == 0) {
      createTestMethod(propertyName, window[propertyName]);
    } else if (propertyName.indexOf('setUp') == 0) {
      testCaseForFile.prototype.setUp = window[propertyName];
    } else if (propertyName.indexOf('tearDown') == 0) {
      testCaseForFile.prototype.tearDown = window[propertyName];
    }
  }
})();
