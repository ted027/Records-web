import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import VisibleTodoList from './containers/VisibleTodoList';
import AddTodo from './containers/AddTodo';
import Filter from './components/Filter';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import Table from '@material-ui/core/Table';
import Paper from '@material-ui/core/Paper';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableBody from '@material-ui/core/TableBody';
import TableRow from '@material-ui/core/TableRow';

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
        <AppBar
          title="TODO list"
          iconClassNameRight="muidocs-icon-navigation-expand-more"
        />
        <div>
          <AddTodo />
          <Filter />
          <Paper>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>TODO</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                <VisibleTodoList />
              </TableBody>
            </Table>
          </Paper>
        </div>
      </div>
      </MuiThemeProvider>
    );
  }
}

export default App;
