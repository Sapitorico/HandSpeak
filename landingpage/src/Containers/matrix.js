// import React, { useEffect } from 'react';
// import ApexCharts from 'apexcharts';
//
// const ApexChart = ({ confusionMatrix }) => {
//   useEffect(() => {
//     const chartOptions = {
//       chart: {
//         height: '13%',
//         width: '250%',
//         type: 'heatmap',
//       },
//       dataLabels: {
//         enabled: false
//       },
//       colors: ["#008FFB"],
//       title: {
//         text: 'Matriz de confusión'
//       },
//       series: []
//     };
//
//     const generateData = (matrix) => {
//       const series = [];
//       for (let i = 0; i < matrix.length; i++) {
//         const dataRow = [];
//         for (let j = 0; j < matrix[i].length; j++) {
//           let xValue;
//           if (j === 14) {
//             xValue = String.fromCharCode(209); // 'Ñ'
//           } else if (j >= 14) {
//             xValue = String.fromCharCode(65 + j -1);
//           } else {
//             xValue = String.fromCharCode(65 + j);
//           }
//           dataRow.push({
//             x: xValue,
//             y: matrix[i][j]
//           });
//         }
//         let nameValue;
//         if (i === 12) {
//           nameValue = String.fromCharCode(209); // 'Ñ'
//         } else if (i >= 12) {
//           nameValue = String.fromCharCode(90 - i + 1);
//         } else {
//           nameValue = String.fromCharCode(90 - i);
//         }
//         series.push({
//           name: nameValue,
//           data: dataRow
//         });
//       }
//       return series;
//     };
//
//     chartOptions.series = generateData(confusionMatrix);
//
//     const chart = new ApexCharts(document.querySelector('#chart'), chartOptions);
//     chart.render();
//
//     return () => {
//       chart.destroy();
//     };
//   }, [confusionMatrix]);
//
//   return (
//     <div id="chart" style={{ width: '15rem', height: '15rem' }} />
//   );
// };
//
// export default ApexChart;
import React, { useEffect } from 'react';
import ApexCharts from 'apexcharts';

const ConfusionMatrix = ({ confusionMatrix }) => {
  useEffect(() => {
    const chartOptions = {
      chart: {
        height: '13%',
        width: '250%',
        type: 'heatmap',
      },
      dataLabels: {
        enabled: false
      },
      colors: ['#E60026'], // Color gris para cuadritos vacíos
      title: {
        text: 'Matriz de confusión'
      },
      series: [],
      plotOptions: {
        heatmap: {
          shadeIntensity: 0.5,
          colorScale: {
            ranges: [
              {
                from: 0,
                to: 0,
                name: 'Vacios',
                color: '#808080' // Color gris para cuadritos vacíos
              },
              {
                from: 1,
                to: 100,
                name: 'Llenos',
                color: '#E60026' // Color rubí para cuadritos llenos
              }
            ]
          }
        }
      }
    };

    const generateData = (matrix) => {
      const series = [];
      for (let i = 0; i < matrix.length; i++) {
        const dataRow = [];
        for (let j = 0; j < matrix[i].length; j++) {
          let xValue;
          if (j === 14) {
            xValue = String.fromCharCode(209); // 'Ñ'
          } else if (j >= 14) {
            xValue = String.fromCharCode(65 + j -1);
          } else {
            xValue = String.fromCharCode(65 + j);
          }
          dataRow.push({
            x: xValue,
            y: matrix[i][j],
            fillColor: matrix[i][j] === 0 ? '#808080' : '#E60026' // Asignar color gris o rubí según si está lleno o vacío
          });
        }
        let nameValue;
        if (i === 12) {
          nameValue = String.fromCharCode(209); // 'Ñ'
        } else if (i >= 12) {
          nameValue = String.fromCharCode(90 - i + 1);
        } else {
          nameValue = String.fromCharCode(90 - i);
        }
        series.push({
          name: nameValue,
          data: dataRow
        });
      }
      return series;
    };

    chartOptions.series = generateData(confusionMatrix);

    const chart = new ApexCharts(document.querySelector('#chart'), chartOptions);
    chart.render();

    return () => {
      chart.destroy();
    };
  }, [confusionMatrix]);

  return (
    <div id="chart" style={{ width: '15rem', height: '15rem' }} /> // Ajustar el ancho para que los cuadritos se vean correctamente
  );
};

export default ConfusionMatrix;
