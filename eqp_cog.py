import kcs_dex
import kcs_ui
import kcs_util
import os
import datetime
import aadAssDataExtraction
   
def main():
    dataExtra = aadAssDataExtraction.DataExtraction()
    
    temp_file = '%s\\%s.txt'%(os.environ['TEMP'] ,datetime.datetime.now().strftime('%y%m%d%H%M%S'))
    f = open(temp_file,'w')
    f.writelines('%20s %20s %20s %20s %20s %20s\n'%('设备名', '重量', 'X','Y','Z','模块'))
    res, input_name = kcs_ui.string_req('请输入设备名称','')
    if res == kcs_util.ok():
        dex_str = "EQUIPMENT.ITEM('%s'*).NAME"% input_name
        dataExtra.ExtractData(dex_str)
        
        eqp_name_list = dataExtra.DataResult
        for eqp_name in eqp_name_list:
        
            dex_str = "EQUIPMENT.ITEM('%s').REFERENCE.POINT"% eqp_name
            dataExtra.ExtractData(dex_str)
            ref_point = dataExtra.DataResult[0]
            
            dex_str = "EQUIPMENT.ITEM('%s').COMP_NAME"% eqp_name
            dataExtra.ExtractData(dex_str)
            comp_name = dataExtra.DataResult[0]
            weight = 0
            
            dex_str = "COMPONENT('%s').GEN_PROPERTY.WEIGHT"%comp_name
            dataExtra.ExtractData(dex_str)
            weight = dataExtra.DataResult[0]

            dex_str = "EQUIPMENT.ITEM('%s').MODULE(*).NAME"%eqp_name
            dataExtra.ExtractData(dex_str)
            mod_name = dataExtra.DataResult[0]
            
            f.writelines('%20s %20s %20s %20s %20s %20s\n'%(eqp_name,round(weight), round(ref_point[0]),round(ref_point[1]),round(ref_point[2]),mod_name))
    f.close()
    os.startfile(temp_file)
            
if __name__ == "__main__":
    main()
            

            