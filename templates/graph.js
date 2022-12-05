Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: '5 Components with the highest fail rate	'
    },
    subtitle: {
        text: 'Source: <a href="https://worldpopulationreview.com/world-cities" target="_blank"></a>'
    },
    xAxis: {
        type: 'category',
        labels: {
            rotation: -45,
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Fail Rate'
        }
    },
    legend: {
        enabled: false
    },
    tooltip: {
        pointFormat: 'Population in 2021: <b>{point.y:.1f} millions</b>'
    },
    series: [{
        name: 'worst_components',
        data: [
            ['windshield	', 0.2],
            ['light	', 0.08],
            ['brake	', 0.02],
            ['speaker	', 0.02],
            ['tire	', 0.01],



        ],
        dataLabels: {
            enabled: true,
            rotation: 0,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y:.2f}', // one decimal
            y: 10, // 10 pixels down from the top
            style: {
                fontSize: '11px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    }]
});
