import fs from "fs";
import path from "path";
import { spawnSync } from "child_process";

// Minimal ARIMA-style forecast stub; replace with proper model when dependency is available.
export function forecastCashFlow(series: number[], months: number): number[] {
  if (!series.length) return Array(months).fill(0);
  const avg = series.reduce((a, b) => a + b, 0) / series.length;
  return Array.from({ length: months }).map((_, idx) => avg * (1 + idx * 0.02));
}

export function renderForecastTable(values: number[]): string {
  const rows = values.map((value, i) => `M${i + 1}\t${value.toFixed(2)}`);
  return ["# Cash-Flow Forecast", ...rows].join("\n");
}

export function writeForecastReport(outputDir: string, data: number[]): string {
  fs.mkdirSync(outputDir, { recursive: true });
  const filePath = path.join(outputDir, "forecast.txt");
  fs.writeFileSync(filePath, renderForecastTable(data));
  return filePath;
}

export function runCli(series: number[], months: number): void {
  const data = forecastCashFlow(series, months);
  console.log(renderForecastTable(data));
}

export function runPostbuildBeacon(scriptPath = "scripts/postbuild.py"): void {
  const result = spawnSync("python", [scriptPath]);
  if (result.status !== 0) {
    throw new Error(`Beacon generation failed: ${result.stderr.toString()}`);
  }
}

if (require.main === module) {
  runCli([1200, 1350, 980], 6);
}
