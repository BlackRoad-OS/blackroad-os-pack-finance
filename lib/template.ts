/**
 * Template utilities for finance pack.
 */

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
