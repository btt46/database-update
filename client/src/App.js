import React, { Component } from 'react';
import './App.css';
import Axios from 'axios';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      status: '',
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  update = state => {
    Axios.post('http://127.0.0.1:5000/update', {
      email: state.email,
      new_status: state.status,
    }).then(function(res) {
      alert(res.data.result);
    })
  };

  handleSubmit = event => {
    this.update(this.state)
    event.preventDefault();
  };  

  handleChange = event => {
    const value = event.target.value
    const key = event.target.name
    this.setState({ [key]: value });
  };

  render() {
    return (
      <div className="App">
        <header className="App-header">
            <h1>Updating</h1>
            <form onSubmit={this.handleSubmit}>
              <div><label>
                Email: <br />
                <input name="email"
                     type="text"
                     value={this.state.email}     
                     onChange={this.handleChange} />
              </label></div>
              <div><label>
                Status: <br />
                <input name="status"
                     type="text"
                     value={this.state.status}     
                     onChange={this.handleChange} />
              </label></div>
              <input type="submit" value="Update" />
            </form>
        </header>
      </div>
    );
  }
}