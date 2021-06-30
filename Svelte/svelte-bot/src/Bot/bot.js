export function scrapeIMDB(name) {
  const puppeteer = require("puppeteer");
  (async () => {
    const browser = await puppeteer.launch({
      headless: true,
      args: [
        "--no-sandbox",
        "--disable-dev-shm-usage", // <-- add this one
      ],
    });
    const page = await browser.newPage();
    await page.goto("https://imdb.com");
    const [input] = await page.$x("//div[@role='combobox']/input");
    if (input) {
      await input.click();
      input.type(name);
      await page.waitForTimeout(3000);
      const [result] = await page.$x(
        "//ul[@role='listbox']/li[@role='option']"
      );
      if (result) {
        result.click();
      }
    }
    console.log("finished");
  })();
}
