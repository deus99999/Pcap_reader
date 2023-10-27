import pandas as pd
from reader import read_pcap

# data_frame = pd.json_normalize(read_pcap())

print(read_pcap())
class GetData:
    def __init__(self, frame):
        self.frame = frame

    def get_position(self):
        while True:
            data_frame = pd.json_normalize(read_pcap())[['100.X', '100.Y', '136.MFL']]
            # data_frame = pd.Series(['100.X', '100.Y', '136.MFL'])
            return data_frame

    def get_correlated(self):
        """В контексте навигации "коррелированные координаты" могут относиться к системе координат, которая согласована
        с глобальной системой координат, например, географическими координатами широты и долготы."""
        data_frame = pd.json_normalize(read_pcap())[['105.Lat', '105.Lon']]
        return data_frame

        # lst = []
        # x = self.frame.loc[0, '100.X']
        # y = self.frame.loc[0, '100.Y']
        # mfl = self.frame.loc[0, '136.MFL']
        #
        # lst.append(x)
        # lst.append(y)
        # lst.append(mfl)
        # # df = pd.Series([x, y, mfl])
        # return lst
        # return df.to_string(index=False)


d = GetData(read_pcap)
print(d.get_position())

    # def get_sac(self):
    #     return self.data_csv.iloc[0, '010.SAC']
    #
    # def get_sic(self):
    #     return self.data_csv.loc[0, '010.SIC']
    #
    # def get_sid(self):
    #     return self.data_csv.loc[0, '015.SID']
    #
    # def get_tot(self):
    #     return self.data_csv.loc[0, '070.ToT']
    #
    # def get_lat(self):
    #     return self.data_csv.loc[0, '105.Lat']
    #
    # def get_lon(self):
    #     return self.data_csv.loc[0, '105.Lon']
    #
    # def get_X(self):
    #     return self.data_csv.loc[0, '100.X']
    #
    # def get_Y(self):
    #     return self.data_csv.loc[0, '100.Y']
    #
    # def get_Vx(self):
    #     return self.data_csv.loc[0, '185.Vx']
    #
    # def get_Vy(self):
    #     return self.data_csv.loc[0, '185.Vy']
    #
    # def get_Ax(self):
    #     return self.data_csv.loc[0, '210.Ax']
    #
    # def get_Ay(self):
    #     return self.data_csv.loc[0, '210.Ay']
    #
    # def get_V(self):
    #     return self.data_csv.loc[0, '060.V']
    #
    # def get_G(self):
    #     return self.data_csv.loc[0, '060.G']
    #
    # def get_CH(self):
    #     return self.data_csv.loc[0, '060.CH']
    #
    # def get_spare_Track_Mode_3A_Code(self):
    #     return self.data_csv.loc[0, '060.spare']
    #
    # def get_Mode3A(self):
    #     return self.data_csv.loc[0, '060.Mode3A']
    #
    # def get_ADR(self):
    #     return self.data_csv.loc[0, '380.ADR']
    #
    # def get_ACID(self):
    #     return self.data_csv.loc[0, '380.ACID']
    #
    # def get_MAH(self):
    #     return self.data_csv.loc[0, '380.MAH']
    #
    # def get_TAS(self):
    #     return self.data_csv.loc[0, '380.TAS']
    #
    # def get_SAS(self):
    #     return self.data_csv.loc[0, '380.SAS']
    #
    # def get_SRC(self):
    #     return self.data_csv.loc[0, '380.SRC']
    #
    # def get_Alt(self):
    #     return self.data_csv.loc[0, '380.Alt']
    #
    # def get_MV(self):
    #     return self.data_csv.loc[0, '380.MV']
    #
    # def get_AH(self):
    #     return self.data_csv.loc[0, '380.AH']
    #
    # def get_AM(self):
    #     return self.data_csv.loc[0, '380.AM']
    #
    # def get_BVR(self):
    #     return self.data_csv.loc[0, '380.BVR']
    #
    # def get_GVR(self):
    #     return self.data_csv.loc[0, '380.GVR']
    #
    # def get_RAN(self):
    #     return self.data_csv.loc[0, '380.RAN']
    #
    # def get_TI(self):
    #     return self.data_csv.loc[0, '380.TI']
    #
    # def get_spare_ADD(self):
    #     return self.data_csv.loc[0, '380.spare']
    #
    # def get_RoT(self):
    #     return self.data_csv.loc[0, '380.RoT']
    #
    # def get_TAN(self):
    #     return self.data_csv.loc[0, '380.TAN']
    #
    # def get_GS(self):
    #     return self.data_csv.loc[0, '380.GS']
    #
    # def get_IAS(self):
    #     return self.data_csv.loc[0, '380.IAS']
    #
    # def get_MNO(self):
    #     return self.data_csv.loc[0, '380.MNO']
    #
    # def get_BPS(self):
    #     return self.data_csv.loc[0, '380.BPS']
    #
    # def get_TrkN(self):
    #     return self.data_csv.loc[0, '040.TrkN']
    #
    # def get_MON(self):
    #     return self.data_csv.loc[0, '080.MON']
    #
    # def get_SPI(self):
    #     return self.data_csv.loc[0, '080.SPI']
    #
    # def get_MRH(self):
    #     return self.data_csv.loc[0, '080.MRH']
    #
    # def get_SRC(self):
    #     return self.data_csv.loc[0, '080.SRC']
    #
    # def get_CNF(self):
    #     return self.data_csv.loc[0, '080.CNF']
    #
    # def get_FX(self):
    #     return self.data_csv.loc[0, '080.FX']
    #
    # def get_SIM(self):
    #     return self.data_csv.loc[0, '080.SIM']
    #
    # def get_TSE(self):
    #     return self.data_csv.loc[0, '080.TSE']
    #
    # def get_TSB(self):
    #     return self.data_csv.loc[0, '080.TSB']
    #
    # def get_FPC(self):
    #     return self.data_csv.loc[0, '080.FPC']
    #
    # def get_AFF(self):
    #     return self.data_csv.loc[0, '080.AFF']
    #
    # def get_STP(self):
    #     return self.data_csv.loc[0, '080.STP']
    #
    # def get_KOS(self):
    #     return self.data_csv.loc[0, '080.KOS']
    #
    # def get_AMA(self):
    #     return self.data_csv.loc[0, '080.AMA']
    #
    # def get_MD4(self):
    #     return self.data_csv.loc[0, '080.MD4']
    #
    # def get_ME(self):
    #     return self.data_csv.loc[0, '080.ME']
    #
    # def get_MI(self):
    #     return self.data_csv.loc[0, '080.MI']
    #
    # def get_MD5(self):
    #     return self.data_csv.loc[0, '080.MD5']
    #
    # def get_CST(self):
    #     return self.data_csv.loc[0, '080.CST']
    #
    # def get_PSR(self):
    #     return self.data_csv.loc[0, '080.PSR']
    #
    # def get_SSR(self):
    #     return self.data_csv.loc[0, '080.SSR']
    #
    # def get_MDS_TS(self):
    #     """080 Track Status"""
    #     return self.data_csv.loc[0, '080.MDS']
    #
    # def get_ADS(self):
    #     return self.data_csv.loc[0, '080.ADS']
    #
    # def get_SUC(self):
    #     return self.data_csv.loc[0, '080.SUC']
    #
    # def get_AAC(self):
    #     return self.data_csv.loc[0, '080.AAC']
    #
    # def get_SDS(self):
    #     return self.data_csv.loc[0, '080.SDS']
    #
    # def get_EMS(self):
    #     return self.data_csv.loc[0, '080.EMS']
    #
    # def get_PFT(self):
    #     return self.data_csv.loc[0, '080.PFT']
    #
    # def get_FPLT(self):
    #     return self.data_csv.loc[0, '080.FPLT']
    #
    # def get_SSR(self):
    #     return self.data_csv.loc[0, '290.SSR']
    #
    # def get_MDS_STUA(self):
    #     """290 System Track Update Ages"""
    #     return self.data_csv.loc[0, '290.MDS']
    #
    # def get_TRANSA(self):
    #     return self.data_csv.loc[0, '200.TRANSA']
    #
    # def get_LONGA(self):
    #     return self.data_csv.loc[0, '200.LONGA']
    #
    # def get_VERTA(self):
    #     return self.data_csv.loc[0, '200.VERTA']
    #
    # def get_ADF(self):
    #     return self.data_csv.loc[0, '200.ADF']
    #
    # def get_spare_TDA(self):
    #     """200 Track Data Ages"""
    #     return self.data_csv.loc[0, '200.spare']
    #
    # def get_MFL_TDA(self):
    #     """295 Track Data Ages"""
    #     return self.data_csv.loc[0, '295.MFL']
    #
    # def get_MDA(self):
    #     """295 Track Data Ages"""
    #     return self.data_csv.loc[0, ' 295.MDA']
    #
    # def get_MFL_MFL(self):
    #     """136 Measured Flight Level"""
    #     return self.data_csv.loc[0, '136.MFL']
    #
    # def get_QNH(self):
    #     return self.data_csv.loc[0, '135.QNH']
    #
    # def get_CTBA(self):
    #     return self.data_csv.loc[0, '135.CTBA']
    #
    # def get_RoC(self):
    #     return self.data_csv.loc[0, '220.RoC']


# data_csv = pd.read_csv('data_csv.csv')


