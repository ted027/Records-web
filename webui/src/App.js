import React, { Component } from 'react';
import './App.css';
import Table from './components/Table';
import { MuiThemeProvider, createMuiTheme } from 'material-ui/styles';
import yellow from '@material-ui/core/colors/yellow'

const theme = createMuiTheme({
  overrides: {
    MuiTableSortLabel: {
      root: {
        color: yellow,
      },
      active: {
        color: yellow,
      }
    }
  }
});

class App extends Component {
  render() {
    return (
      <MuiThemeProvider theme={theme}>
      <div className="App">
          <Table />
      </div>
      </MuiThemeProvider>
    );
  }
}

export default App;
