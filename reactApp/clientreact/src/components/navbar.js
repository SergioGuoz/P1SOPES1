import React, {Component} from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'


class Navegador extends Component{
    render(){
        return <Navbar bg="light" variant="light">
          
        <Navbar.Brand href="#">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRO9inxUVhYWQpv27oj4cBgWE6J9gpKIxMeNQ&usqp=CAU"
            width="30"
            height="30"
            className="d-inline-block align-top"
            alt="React Bootstrap logo"
          />
          Ingeniería</Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link href="#">Ciencias y Sistemas</Nav.Link>
        </Nav>
        
      </Navbar>

    }
}

export default Navegador