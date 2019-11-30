import React, { Component } from 'react';
import { Select, Card, List, Table, Divider, Tag, Row, Col } from 'antd';
import "antd/dist/antd.css";

import axios from 'axios';
const { option } = Select;

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
      title: 'Available',
      key: 'is_available',
      dataIndex: 'is_available',
      render: text => text === false ? <Tag color="volcano">NO</Tag> : <Tag color="green">YES</Tag>
    },
    {
      title: 'Action',
      key: 'action',
    },
  ];

class GetResult extends Component{
    constructor(props){
        super(props)

        this.state ={
            categories: [],
        };

    }

    componentDidMount(){
        axios.get('http://127.0.0.1:8000/api/results/')
            .then( res => {
                const categories = res.data;
                this.setState({
                    categories:categories
                });
            })
        
        console.log(this.state.categories)
    }

    render(){
        const categories = this.state.categories;
        const cardList = [];

        for(let i=0; i< categories.length; i++){
            cardList.push(
                <Row gutter={16} style={{ background: "#833ab4;", background:"-webkit-linear-gradient(to right, #fcb045, #fd1d1d, #833ab4)", background:"linear-gradient(to right, #fcb045, #fd1d1d, #833ab4)" }}>
                    <Col className="gutter-row" span={2} >
                        <div className="gutter-box">
                            <Card title={categories[i].name} style={{ width: 200 }}>
                            <p>Card content</p>
                            </Card>
                        </div>
                    </Col>
                </Row>
            )
        }

        return(
            <div>
                <Table columns={columns} dataSource={this.state.categories}></Table>
            </div>
        )
    }
}


export default GetResult;