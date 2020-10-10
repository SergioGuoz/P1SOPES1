import React, { useState, Component } from 'react'
import {Scatter,Line} from 'react-chartjs-2'
import axios from 'axios'


class GraficaCPU extends Component{

    constructor(props){
        super(props);        
        var datosA=[];
        var datosB=[];
        this.state={
            cantidadA:0,
            cantidadB:0,
            datosA:[],
            datosB:[],
            chartData:{
                labels:Array.from(new Array(10),(_,i)=>(i===0?1:i)),
                datasets : [{
                    label: 'CPU A',
                    data: datosA,
                    backgroundColor:"rgba(65,174,245,0.4)"
                },{
                    label:'CPU B',
                    data: datosB,
                    backgroundColor:"rgba(245,106,65,0.5)"
                }]
            }
        }
    }

    componentDidMount() {
        this.interval = setInterval(() => 
        {
            let url='http://34.72.179.225:3000/cpu';
            let urlb='http://35.223.45.137:3000/cpu';


            axios.get(url)
            .then(response=>{
                console.log(response.data);
                let {datosA,datosB,cantidadA}=this.state;

                if(datosA.length>=10){datosA=[]}
                
                cantidadA=cantidadA+1
                
                datosA.push({x:cantidadA,y:parseInt(response.data.cpu)})
                console.log("insetando ",datosA);
                this.setState({
                    cantidadA:cantidadA,
                    datosA:datosA,
                    datosB:datosB,
                    chartData:{
                        labels:Array.from(new Array(10),(_,i)=>(i===0?1:i)),
                        datasets : [{
                            label: 'CPU A',
                            data: datosA,
                            backgroundColor:"rgba(65,174,245,0.4)",
                            scaleOverride: true,
                            scaleSteps: 10,
                        },{
                            label:'CPU B',
                            data: datosB,
                            backgroundColor:"rgba(245,106,65,0.5)",
                            scaleOverride: true,
                            scaleSteps: 10,
                        }]
                    }
                }
                    
                )
            }).catch(error=>{
                console.log("ERROR ",error)
                this.setState({errorMsg:'Sin datos',notas:[]})
            });

            axios.get(urlb)
            .then(response=>{
                console.log(response.data);
                let {datosA,datosB,cantidadA}=this.state;

                if(datosB.length>=10){datosB=[]}
                                
                datosB.push({x:cantidadA,y:parseInt(response.data.cpu)})
                this.setState({
                    datosA:datosA,
                    datosB:datosB,
                    chartData:{
                        labels:Array.from(new Array(10),(_,i)=>(i===0?1:i)),
                        datasets : [{
                            label: 'CPU A',
                            data: datosA,
                            backgroundColor:"rgba(65,174,245,0.4)"
                        },{
                            label:'CPU B',
                            data: datosB,
                            backgroundColor:"rgba(245,106,65,0.5)"
                        }]
                    }
                }
                    
                )
            }).catch(error=>{
                console.log("ERROR ",error)
            })
        }
        , 5000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render(){
        return(
            <div className="chart" style={{"backgroundColor":"white"}}>
                <Line
                    data={this.state.chartData}
                    width={500}
                    height={400}
                    options={{
                        title:{
                            display:true,
                            text:"CPU",
                            fontSize:20
                        },
                        yAxes: [{
                            ticks: {
                                max: 2000,
                                min: 1300,
                                stepSize: 10
                            }
                        }],
                        xAxes:[
                            {
                                gridLines:false,
                                ticks:{
                                    callback(tick,index){
                                        return index %7 !==0?"":tick;
                                    }
                                }
                            }
                        ]
                    }}
                    redraw
                    ref = {(reference) => this.reference = reference}
                />
            </div>
        )
    }
}

export default GraficaCPU;
