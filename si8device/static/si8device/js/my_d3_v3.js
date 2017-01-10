/**
 * Created by a.zaikin on 10.01.2017.
 */

bisectDate = d3.bisector(function (d) {
    return d.date;
}).left;

//canvass.each(function (p, j) {
//    var canvas = d3.select(this);
//    var url = canvas.attr('data-url');
//    getChart(canvas, url);
//})

class ChartD3{

    constructor(canvas, url){
        //this.data1 = null;
        this.context = canvas.node().getContext("2d");
        d3.json(url, function (error, json) {
            if (error) return console.warn(error);
            this.data2 = json;
        });

        this.x = d3.scaleTime()
            .range([0, 700])
            .x.domain(d3.extent(data2, function (d) {
                d.date = parseTime_json(d.date);
                return d.date;
            }));

        this.y = d3.scaleLinear()
            .range([30, 0])
            .domain(d3.extent(data2, function (d) {
                return d.close;
            }));

        this.line = d3.line()
            .x(function (d) {
                return x(d.date);
            })
            .y(function (d) {
                return y(d.close);
            })
            .curve(d3.curveStep)
            .context(this.context);


        this.context.beginPath();
        line(data2);
        this.context.lineWidth = 1.5;
        this.context.strokeStyle = "steelblue";
        this.context.stroke();
    }


    static getPoint(point){
        var x0 = x.invert(point[0]),
            i = bisectDate(data2, x0, 1),
            y0 = data1[i].close;
        return {"x":x0, 'y':y0 }
    }

}

//var parseTime = d3.timeParse("%d-%b-%y");
var parseTime_json = d3.timeParse("%H:%M");
var canvas = d3.select("body").select("canvas");
var url = canvas.attr('data-url');
var my_chartd3 = new ChartD3(canvas, url);