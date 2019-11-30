import React from 'react';
import logo from './logo.svg';
import './App.css';
import "antd/dist/antd.css";
import GetCategory from './components/getResult';
import { Layout, Input, Row, Col } from 'antd';

const { Header, Footer, Content, Sider } = Layout;
const { Search } = Input;

function App() {
  return (
    <div className="App">
      <Layout>
        <Header style={{ background: "#833ab4;", background:"-webkit-linear-gradient(to right, #fcb045, #fd1d1d, #833ab4)", background:"linear-gradient(to right, #fcb045, #fd1d1d, #833ab4)"}}>
          <Search
            placeholder="input search text"
            onSearch={value => console.log(value)}
            style={{ width: 500 }}
          />
        </Header>
        <Content>
          <GetCategory></GetCategory>
        </Content>
        <Footer style={{ background: "#833ab4;", background:"-webkit-linear-gradient(to right, #fcb045, #fd1d1d, #833ab4)", background:"linear-gradient(to right, #fcb045, #fd1d1d, #833ab4)"}}>
          Footer
        </Footer>
      </Layout>
    </div>
  );
}

export default App;
