import React from 'react';
import logo from './logo.svg';
import './App.css';
import "antd/dist/antd.css";
import GetCategory from './components/getCategory';
import { Layout, Input, Row, Col } from 'antd';
import Sider from 'antd/lib/layout/Sider';

const { Header, Footer, Content } = Layout;
const { Search } = Input;

function App() {
  return (
    <div className="App">
      <Layout>
        <Header>
          <Search
            placeholder="input search text"
            onSearch={value => console.log(value)}
            style={{ width: 500 }}
          />
        </Header>
        <Content>
          <Row gutter={[8, 8]}>
            <Col span={8} >
              <GetCategory></GetCategory>
            </Col>
            <Col span={16} >
              
            </Col>
          </Row>
        </Content>
        <Footer style={{ background: "#001529"}}>
          Footer
        </Footer>
      </Layout>
    </div>
  );
}

export default App;
