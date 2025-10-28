const { Builder, By, until } = require('selenium-webdriver');

(async function testCounter() {
  let driver = await new Builder().forBrowser('chrome').build();

  try {
    // ✅ Corrected local HTML file path
    await driver.get('file:///C:/Student/devops%20lab/selenium-demo/index.html');

    // ✅ Wait for the elements to appear
    const counter = await driver.wait(until.elementLocated(By.id('counter')), 5000);
    const button = await driver.wait(until.elementLocated(By.id('increment-btn')), 5000);

    // Check initial value is 0
    let countText = await counter.getText();
    console.log('Initial counter:', countText);

    // Click the increment button
    await button.click();

    // Wait until the counter text changes to '1'
    await driver.wait(until.elementTextIs(counter, '1'), 5000);

    countText = await counter.getText();
    console.log('Counter after click:', countText);

    if (countText === '1') {
      console.log('✅ Test passed!');
    } else {
      console.log('❌ Test failed.');
    }
  } catch (err) {
    console.error('❌ Error:', err);
  } finally {
    await driver.quit();
  }
})();
