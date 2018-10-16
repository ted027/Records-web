import React, { Component } from 'react';
import './App.css';
import Table from './components/Table';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

class App extends Component {
  render() {
    return (
      <MuiThemeProvider>
      <div className="App">
          <Table />
      </div>
      </MuiThemeProvider>
    );
  }
}

export default App;
