import React, { Component } from 'react';
import { Select, Card, List, Table, Divider, Tag } from 'antd';
import "antd/dist/antd.css";

import axios from 'axios';
const { option } = Select;

class GetCategory extends Component{
    constructor(props){
        super(props)

        this.state ={
            categories: [],
        };

    }

    componentDidMount(){
        axios.get('http://127.0.0.1:8000/api/categories/')
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
                <Card title={categories[i].name} style={{ width: 200 }}>
                    <p>Card content</p>
                </Card>
            )
        }

        return(
            <div>
                {cardList}
            </div>
        )
    }
}


export default GetCategory;