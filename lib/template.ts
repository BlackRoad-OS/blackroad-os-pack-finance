import fs from "fs";
import Handlebars from "handlebars";

export function renderTemplate(templatePath: string): string {
  const source = fs.readFileSync(templatePath, "utf8");
  const template = Handlebars.compile(source);
  return template({ period: "2025-11", month: "2025-11" });
}

if (require.main === module) {
  const file = process.argv[2];
  if (!file) {
    throw new Error("Template path required");
  }
  const output = renderTemplate(file);
  process.stdout.write(output);
}
