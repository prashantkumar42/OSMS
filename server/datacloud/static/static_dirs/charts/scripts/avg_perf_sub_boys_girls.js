function avg_perf_sub_boys_girls(container_name, data_final) {
    console.log(data_final);
    Highcharts.chart(container_name, {
            chart: {
                type: 'line',
                zoomType: 'x y'
            },
            title: {
                text: 'Average Performance'
            },

            subtitle: {
                text: ''
            },

            xAxis: {
                categories: data_final.Categories,
                labels: {
                    formatter: function () {
                        return this.value;
                    }
                }
            },

            yAxis: {
                min: 0,
                max: 100,
                tickInterval: 10,
                title: {
                    text: 'Percentage (%)'
                },
            },

            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle'
            },

            tooltip: {
                headerFormat: '',
                pointFormat: '{series.name}: {point.y}%'
            },

            plotOptions: {
                line: {
                    dataLabels: {
                        enabled: false
                    },
                    enableMouseTracking: true
                }
            },

            series: [
                // {
                //     name: "Girls",
                //     data: data_final.Girls
                // },
                // {
                //     name: "Boys",
                //     data: data_final.Boys
                // },
                {
                    name: "All",
                    data: data_final.All
                },
           ]

        });
}
