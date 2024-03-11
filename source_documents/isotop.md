# ISOTOP Plan-Bee repo
## 《THE BEE BOOK》 

本目录存储ISOTOP发布的智能合约接口，设计理念，和使用场景  
1. ISOTOP1010: 低GAS费ERC721A合约  
2. ISOTOP1011: 可销毁  
3. ISOTOP1012: 可租借 
4. ISOTOP1013: 可租借可销毁  
5. ISOTOP1014: 跨链资产转移合约  
6. ISOTOP1015: 单一图像徽章NFT合约，兼容ISOTOP1010   
7. ISOTOP1016: 动态NFT   
8. ISOTOP1017: NFT藏品，支持顺序铸造和按照编号铸造 
9. ISOTOP1018：单一图片ERC721 POAP徽章合约
10. ISOTOP1019：兼容ERC1155的数藏品合约
11. ISOTOP101A: 单一图片ERC1155 POAP徽章合约
12. ISOTOP1030: 预言机调用合约，使用chainlink 预言机，无需LINK，直接使用TGAS费用  
13. ISOTOP1052：票务NFT合约，支持打卡，兼容ERC721
14. DID: 域名解析和身份合约
15. SBT: soulBondToken 灵魂绑定合约，可定制化自己的token metadata
16. SBTII: soulBondToken 灵魂绑定合约，可发行自定义图片的SBT

工具合约：  
1. Deployer : 合约部署器  
2. DDS :  一个通用的域名数据库存储系统  
3. TGas : GAS费用的充账及分配系统  
4. Factory : 合约工厂，可以通过deployContract输入合约名称生产需要的合约, 合约名称见上面列表  
5. DateTime : 一个时间和日期转换工具合约  


## 链支持：

|     chianid    |     链                       |
|----------------|------------------------------|
|     1          |     Conflux Core 测试链      |
|     1029       |     Conflux Core 正式链      |
|     5555       |     武汉链正式链             |
|     12231      |     文昌链测试链             |
|     1224       |     文昌链正式链             |
|     71         |     Conflux eSpace 测试链    |
|     1030       |     Conflux eSpace 正式链    |
|     27         |     草田链正式链             |
|     42161      |     Arbione -正式链          |
|     421613     |     Arbitrum测试链           |
|     97         |     币安测试链               |
|     56         |     币安正式链               |
|     80001      |     Polygon Mumbai测试链     |
|     137        |     Polygon正式链            |
|     5          |     Goerli 以太坊测试链      |
|     1          |     以太坊正式链             |

***
## 合约部署地址：
    "Factory": "0x5067CE4dC9a2fb2c3E1898fc24B067cd8d92A000",  # salt[0]
    "DDS": "0x9E4eE1Cb21DfAA91d513B2BE088338C834DEf001",  # salt[1]
    "DID": "0x7D5D9e9033dF0939c0fc2CD5CE42667Bc2B31002",  # salt[2]
    "Forwarder": "0x0a5d59B18feEd1ef5feB16b302c92AfAc9cbA003",  # salt[3]
    "ERC6551Registry": "0xF6bcf03C6487D1F34e1327263405044BA227C8f4",
    "ERC6551Account": "0x1Fb2690a088B6eE0d4B1646689d46D8afE9a4c8A",
    "ERC6551AccountProxy": "0xFe4f8682D3300D1E5e580a91eaF1BCc7F6B385Ff",
    "String": "0x7142516F3725a711EFEa0Afe90f45b80F88A8713",
    "DateTime": "0x4adc7057e73719857DCDe18E573b1A3B184F612E",
    "List": "0xDBe0b154776c5CEbCdAA399CaF2B89F8649a5e05",
    "BytesUtils": "0xdc5721B288a03f3405f2893E79f87B927C199bDe",
    "Tools": "0x83fB290Bba50BaC4DB1Db93861102c923181AFda",
    'Reset': "0x73Bd86d33E8793161E02Bebc61CDB735Eea8007b",

    "Deployer": "0xb1eFE38b2A51035652631ec27cD634A144B605CC",  # salt 1
    "Admin": "0x82846E3ffEc9f329FCFdE053E29428f3B0CFe20a",  # salt 1
    "Empty": "0x9A62607A54c38b7F672e5Dd41a0B1f7D0a983A21"  # salt 1

*) 主要链为列表中除了以太坊，币安的所有    
*) 其中，Factory已经注册ISOTOP1017-101A, 1052, 1053, DID相关      

***
## 使用方式
参考文档《同位素智能合约对接开发文档.pdf》

last updated: 2023.11.07

Conflux deployment at 2024.1.13
String Contract '0x86e333f6D75a09Ee13C8206847072283F1086a3c' 'cfx:acdsgp9047rax5ux3auguv2hemb9ccdmhug174skbt'
Factory Contract '0x8641e0fb6d1eb2D4f513e3cc079CA27Ec9385922' 'cfx:acded2h5rytnfzhzctv62b66yk9pwsc3ejf1jwaw0h'
ISOTOP1013: 0x8BF6B70F1E309F07061156c92560A7613B64103C 'cfx:acf9rr2td22k8b2gcfnpwknay7ux03auhuu7ey4n0s'


