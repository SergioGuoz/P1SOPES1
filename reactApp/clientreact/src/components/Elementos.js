import React, { Component } from 'react'
import axios from 'axios'
import Card from 'react-bootstrap/Card'
import Button  from 'react-bootstrap/Button';

class Elementos extends Component{
    
    constructor(props){
        super(props)

        this.state={
            notas:[]
        }
    }

    componentDidMount(){
        
    }
    servidoruno(){
        console.log("Presionando Uno");
        
        let url='http://34.72.179.225:3000/elementos';

        axios.get(url)
        .then(response=>{
            console.log(response);
            this.setState({notas:response.data,errorMsg:''})
        }).catch(error=>{
            console.log("ERROR ",error)
            this.setState({errorMsg:'Sin datos',notas:[]})
        })
    }

    servidordos(){
        console.log("Presionando Dos");
        
        let url='http://35.223.45.137:3000/elementos';
        axios.get(url)
        .then(response=>{
            console.log(response.data);  
            this.setState({notas:response.data,errorMsg:''})
        }).catch(error=>{
            console.log("ERROR ",error)
            this.setState({errorMsg:'Sin datos',notas:[]})
        })
    }

    render(){
        const { notas, errorMsg }= this.state;

        return (
            <div>
            <div className="row" style={{"width":"500px","marginTop":"5px"}}>
                <div className="col">
                    <Button variant="outline-light" onClick={()=>this.servidoruno()}>Servidor 1</Button>
                </div>
                <div className="col">
                    <Button variant="outline-light" onClick={()=>this.servidordos()}>Servidor 2</Button>

                </div>
                
            </div>
            <br/>
            PUBLICACIONES
            {
                notas.length ?
                notas.map(infonota =>
                    <Card key={infonota.indice} style={{"width":"500px","marginBottom":"5px"}}>
                        <Card.Header style={{"color":"gray","fontSize":"15px"}}>{infonota.autor}</Card.Header>
                        <Card.Body>
                            <Card.Text  style={{"color":"gray","fontSize":"12px"}}>
                            {infonota.nota}
                            </Card.Text>
                        </Card.Body>
                    </Card>
                    ):
                null
            }
            { errorMsg ? <div>{errorMsg}</div> : null}
            </div>
        )
    }

}

export default Elementos;