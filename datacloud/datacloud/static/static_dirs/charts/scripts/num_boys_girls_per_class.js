function num_boys_girls_per_class(container_name, data_final) {
    Highcharts.chart(container_name, {
            chart: {
                type: 'column',
                zoomType: 'x'
            },
            title: {
                text: 'Number of Students per Class'
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
                title: {
                    text: 'Class Strength'
                },
                stackLabels: {
                    enabled: true,
                    style: {
                        fontWeight: 'bold',
                        color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
                    }
                }
            },
            legend: {
                align: 'right',
                x: -30,
                verticalAlign: 'top',
                y: 25,
                floating: true,
                backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
                borderColor: '#CCC',
                borderWidth: 1,
                shadow: false
            },
            tooltip: {
                headerFormat: '',
                pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
            },
            plotOptions: {
                column: {
                    stacking: 'normal',
                    dataLabels: {
                        enabled: true,
                        color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white'
                    }
                },
                series: {
                    groupPadding: 0,
                    pointPadding: 0.03
                }
            },
            series: [
                {
                    name: "Girls",
                    data: data_final.Girls
                },
                {
                    name: "Boys",
                    data: data_final.Boys
                },
            ]
        }
    );
}
