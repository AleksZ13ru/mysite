/**
 * Created by a.zaikin on 28.07.2016.
 */

var chart = c3.generate({
    bindto: '#chart{{ i }}',
    size: {
        height: 60
    },
    legend: {
        show: false
    },
    axis: {
        x: {
            show: false
        },
        y:{
            show: false
        }
    },
    point: {
        show: false
    },
    data: {
        columns: [
            ['data1',1,1]

        ]
    }
});
