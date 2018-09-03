import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import VisibleTodoList from './containers/VisibleTodoList';
import AddTodo from './containers/AddTodo';
import Filter from './components/Filter';
import Table from './components/Table';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';

const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
});

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
