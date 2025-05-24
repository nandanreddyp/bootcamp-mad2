<template>
  <h2>This is Admin Dashboard</h2>
  <div>
    <canvas id="myChart"></canvas>
    <canvas id="pieChart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'

export default {
  name: 'AdminDashboard',
  data() {
    return {
        names: ['apple', 'banana', 'orange', 'jackfruit'],
        numbers: [10, 20, 30, 40],
    };
  },
  mounted() {
    const ctx = document.getElementById('myChart');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: this.names,
        datasets: [{
          label: '# of Votes',
          data: this.numbers,
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
    const ctxpie = document.getElementById('pieChart');
  new Chart(ctxpie, {
    type: 'pie',
    data: {
      labels: ['Red', 'Blue', 'Yellow'],
      datasets: [{
        label: 'My Dataset',
        data: [300, 50, 100],
        backgroundColor: [
          'rgba(255, 99, 132, 0.7)',
          'rgba(54, 162, 235, 0.7)',
          'rgba(255, 206, 86, 0.7)'
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Pie Chart Example'
        }
      }
    }
  });
  }
}
</script>
