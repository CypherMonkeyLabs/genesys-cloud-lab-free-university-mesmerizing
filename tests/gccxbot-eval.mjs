/* Score the development set. The frozen held-out file is scored by gccxbot-heldout.mjs. */
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";

const here = path.dirname(fileURLToPath(import.meta.url));
const runner = path.join(here, "gccxbot-heldout.mjs");
const result = spawnSync(process.execPath, [
  runner,
  "--spec", path.join(here, "gccxbot-dev.json"),
  "--out", path.join(here, "gccxbot-eval-report.json"),
], { stdio: "inherit" });
process.exit(result.status ?? 1);
