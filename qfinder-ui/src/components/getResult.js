import React, { Component } from 'react';
import { Card, Table, Tag, Row, Col } from 'antd';

import "antd/dist/antd.css";
import { Layout, Input } from 'antd';
import axios from 'axios';

const { Header } = Layout;
const { Search } = Input;

  const columns = [
    {
      title: 'Username',
      dataIndex: 'name',
      key: 'name',
      render: text => <a>{text}</a>,
    },
    {
      title: 'Website',
      dataIndex: 'url',
      key: 'url',
    },
    {
      title: 'Is available?',
      key: 'is_available',
      dataIndex: 'is_available',
      render: text => text === false ? <Tag color="volcano">NO</Tag> : <Tag color="green">YES</Tag>
    },
  ];

class GetResult extends Component{
    constructor(props){
        super(props)

        this.state ={
            results: [],
            loading: false,
        };

    }

    componentDidMount(){

    }

    getSearchResult(username){
        axios({
            method : 'get',
            url: `http://127.0.0.1:8000/api/results/?name=${username}`
        }).then(obj => {
            this.setState({
                results: obj.data,
                loading: false
            });
        })
    }

    searchUsername(username){
        this.setState({
            loading: true
        })
        axios({
            method : 'post',
            url: 'http://127.0.0.1:8000/api/users/', 
            data: {
                name: username,    
            }
        }).then(obj => {
           console.log(obj.data)
           this.getSearchResult(username) 
        })
        
    }

    render(){

        return(
            <div>
                <Header>
                    <Search
                        placeholder="input search text"
                        onSearch={value => this.searchUsername(value)}
                        style={{ width: 500 }}
                        disabled={this.state.loading}
                    />
                </Header>
                <Table size="small" columns={columns} dataSource={this.state.results}></Table>
            </div>
        )
    }
}


export default GetResult;