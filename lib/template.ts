/**
 * Template utilities for finance pack.
 */

import fs from 'fs';
import Handlebars from 'handlebars';

export function formatCurrency(amount: string, currency: string = 'USD'): string {
  const num = parseFloat(amount);
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currency,
  }).format(num);
}

export function formatPercentage(value: string, decimals: number = 2): string {
  const num = parseFloat(value);
  return `${num.toFixed(decimals)}%`;
}

export function generateReportTemplate(title: string, data: Record<string, string | number>): string {
  const lines = [
    `# ${title}`,
    `Generated: ${new Date().toISOString()}`,
    '',
    '## Summary',
    ...Object.entries(data).map(([key, value]) => `- ${key}: ${value}`),
  ];
  return lines.join('\n');
}

export function renderTemplate(templatePath: string, context: Record<string, unknown> = {}): string {
  const source = fs.readFileSync(templatePath, 'utf8');
  const template = Handlebars.compile(source);
  const now = new Date();
  const currentPeriod = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`;
  return template({ period: currentPeriod, month: currentPeriod, ...context });
}

