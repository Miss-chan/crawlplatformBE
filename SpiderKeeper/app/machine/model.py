from SpiderKeeper.app import Base
from SpiderKeeper.app import db


class Serversmachine(Base):

    __tablename__ = 'sk_serversmachine'
    server_ip = db.Column(db.String(50))   # 服务器的ip
    server_status = db.Column(db.String(50))   # 主从服务器运行状态, 0不可用,1可用
    is_master = db.Column(db.String(50))  # 主从服务器的标志, 0从服务器,1主服务器

    def to_dict(self):
        return dict(
            server_ip=self.server_ip,
            server_status=self.server_status,
            is_master=self.is_master
        )