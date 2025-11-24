/**
 * Forecast agent for financial predictions.
 */

import { ForecastResult } from '../models/types';

export interface TimeSeriesData {
  timestamp: string;
  value: string;
}

export class Forecast {
  agentId = 'agent.forecast';
  displayName = 'Forecast';
  packId = 'pack.finance';

  /**
   * Generate simple moving average forecast.
   */
  simpleMovingAverage(data: TimeSeriesData[], window: number = 3): ForecastResult {
    if (data.length < window) {
      throw new Error(`Insufficient data: need at least ${window} points`);
    }

    const recentData = data.slice(-window);
    const sum = recentData.reduce((acc, d) => acc + parseFloat(d.value), 0);
    const average = sum / window;

    const trend = this.detectTrend(data);

    return {
      period: 'next',
      predicted: average.toFixed(2),
      confidence: 0.7,
      trend,
      factors: ['moving_average', `window_${window}`],
    };
  }

  private detectTrend(data: TimeSeriesData[]): 'up' | 'down' | 'stable' {
    if (data.length < 2) return 'stable';

    const recent = parseFloat(data[data.length - 1].value);
    const previous = parseFloat(data[data.length - 2].value);
    const threshold = 0.05; // 5% change threshold

    const change = (recent - previous) / previous;

    if (change > threshold) return 'up';
    if (change < -threshold) return 'down';
    return 'stable';
  }
}

// CLI interface
if (require.main === module) {
  const forecast = new Forecast();
  console.log('Forecast agent initialized:', forecast.agentId);
  // TODO(forecast): Add CLI commands for forecasting operations
}
