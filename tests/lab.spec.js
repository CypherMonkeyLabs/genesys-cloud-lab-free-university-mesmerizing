import { test, expect } from "@playwright/test";
import fs from "node:fs";
import path from "node:path";

const shotDir = path.join("docs", "screenshots");
fs.mkdirSync(shotDir, { recursive: true });

async function quiet(page) {
  await page.addInitScript(() => {
    localStorage.setItem("gccx-tour", "1");
    localStorage.setItem("gccx-greet", "1");
    localStorage.setItem("gccx-bot-stop", "1");
  });
}

test("home, bot, and a lesson at desktop and phone", async ({ page }) => {
  await quiet(page);
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "Genesys Cloud CX Lab" })).toBeVisible();
  await page.screenshot({ path: path.join(shotDir, "wave-home-1440.png"), fullPage: false });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: path.join(shotDir, "wave-home-390.png"), fullPage: false });

  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("/campus/#/lesson/f-sip");
  await expect(page.getByRole("heading", { name: /SIP, RTP/ })).toBeVisible();
  await page.screenshot({ path: path.join(shotDir, "wave-lesson-1440.png"), fullPage: false });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: path.join(shotDir, "wave-lesson-390.png"), fullPage: false });

  await page.setViewportSize({ width: 1440, height: 900 });
  await page.locator("#bot-launcher").click();
  await expect(page.locator("#bot-panel")).toBeVisible();
  await expect(page.locator("#py-chat-input")).toBeVisible();
  await page.screenshot({ path: path.join(shotDir, "wave-bot-1440.png"), fullPage: false });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: path.join(shotDir, "wave-bot-390.png"), fullPage: false });
  await page.locator("[data-py-ask='What is Architect?']").click();
  await expect(page.locator(".py-chat-log")).toContainText(/Architect/i);
});

test("offline reload still opens a lesson and the guide", async ({ page, context }) => {
  await quiet(page);
  await page.goto("/campus/");
  await page.evaluate(async () => {
    await navigator.serviceWorker.ready;
  });
  await page.reload();
  await page.waitForFunction(() => navigator.serviceWorker.controller);
  await context.setOffline(true);
  expect(await page.evaluate(() => navigator.onLine)).toBe(false);
  await page.reload();
  await expect(page.getByRole("heading", { level: 1 }).first()).toBeVisible();
  await page.goto("/campus/#/lesson/f-sip");
  await expect(page.getByRole("heading", { name: /SIP, RTP/ })).toBeVisible();
  await page.locator("#bot-launcher").click();
  await page.locator("#py-chat-input").fill("What is SIP?");
  await page.locator(".py-chat-form button[type='submit']").click();
  await expect(page.locator(".py-chat-log")).toContainText(/SIP/i);
});
