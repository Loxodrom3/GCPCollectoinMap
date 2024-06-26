import os
import shutil
import numpy as np

srcPath  = ("C:\C_Temp\change")

dstPath =  ("C:\C_Temp\Change\out")
PIDArr   = np.array (["VNM000001", "VNM000002", "VNM000003", "VNM000004", "VNM000005", "VNM000006", "VNM000007", "VNM000008", "VNM000009", "VNM000010", "VNM000011", "VNM000012", "VNM000013", "VNM000015", "VNM000016", "VNM000017", "VNM000018", "VNM000019", "VNM000020", "VNM000021", "VNM000022", "VNM000023", "VNM000024", "VNM000025", "VNM000026", "VNM000027", "VNM000028", "VNM000029", "VNM000030", "VNM000031", "VNM000032", "VNM000033", "VNM000034", "VNM000035", "VNM000036", "VNM000037", "VNM000038", "VNM000039", "VNM000040", "VNM000041", "VNM000042", "VNM000043", "VNM000044", "VNM000045", "VNM000046", "VNM000047", "VNM000048", "VNM000049", "VNM000050", "VNM000051", "VNM000052", "VNM000053", "VNM000054", "VNM000055", "VNM000057", "VNM000058", "VNM000059", "VNM000060", "VNM000061", "VNM000062", "VNM000063", "VNM000064", "VNM000065", "VNM000066", "VNM000067", "VNM000068", "VNM000069", "VNM000070", "VNM000071", "VNM000072", "VNM000073", "VNM000074", "VNM000075", "VNM000076", "VNM000077", "VNM000078", "VNM000079", "VNM000080", "VNM000081", "VNM000082", "VNM000083", "VNM000084", "VNM000085", "VNM000086", "VNM000087", "VNM000088", "VNM000089", "VNM000090", "VNM000091", "VNM000092", "VNM000093", "VNM000094", "VNM000095", "VNM000096", "VNM000097", "VNM000098", "VNM000099", "VNM000100", "VNM000101", "VNM000102", "VNM000103", "VNM000104", "VNM000105", "VNM000106", "VNM000107", "VNM000108", "VNM000109", "VNM000110", "VNM000111", "VNM000112", "VNM000113", "VNM000114", "VNM000115", "VNM000116", "VNM000117", "VNM000118", "VNM000119", "VNM000120", "VNM000121", "VNM000122", "VNM000123", "VNM000124", "VNM000125", "VNM000126", "VNM000127", "VNM000128", "VNM000129", "VNM000130", "VNM000131", "VNM000132", "VNM000133", "VNM000134", "VNM000135", "VNM000136", "VNM000137", "VNM000138", "VNM000139", "VNM000140", "VNM000141", "VNM000142", "VNM000143", "VNM000144", "VNM000145", "VNM000146", "VNM000147", "VNM000148", "VNM000149", "VNM000150", "VNM000151", "VNM000152", "VNM000153", "VNM000154", "VNM000155", "VNM000156", "VNM000157", "VNM000158", "VNM000160", "VNM000161", "VNM000162", "VNM000163", "VNM000166", "VNM000167", "VNM000168", "VNM000175", "VNM000176", "VNM000180", "VNM000181", "VNM000186", "VNM000187", "VNM000192", "VNM000193", "VNM000198", "VNM000199", "VNM000205", "VNM000211", "VNM000212", "VNM000218", "VNM000224", "VNM000225", "VNM000229", "VNM000230", "VNM000301", "VNM000302", "VNM000303", "VNM000056", "VNM000159", "VNM000164", "VNM000165", "VNM000169", "VNM000170", "VNM000171", "VNM000172", "VNM000173", "VNM000174", "VNM000177", "VNM000178", "VNM000179", "VNM000182", "VNM000183", "VNM000184", "VNM000185", "VNM000188", "VNM000189", "VNM000190", "VNM000191", "VNM000194", "VNM000195", "VNM000196", "VNM000197", "VNM000200", "VNM000201", "VNM000202", "VNM000203", "VNM000204", "VNM000206", "VNM000207", "VNM000208", "VNM000209", "VNM000210", "VNM000213", "VNM000214", "VNM000215", "VNM000216", "VNM000217", "VNM000219", "VNM000220", "VNM000221", "VNM000222", "VNM000223", "VNM000226", "VNM000227", "VNM000228", "VNM000231", "VNM000300", "VNM000304", "TJK100012", "TJK100013", "TJK100014", "TJK100014A", "TJK100015", "TJK100016", "TJK100017", "TJK100023", "TJK100024", "TJK100025", "TJK100029", "TJK100030", "TJK100034", "TJK100035", "TJK100036", "TJK100037", "TJK100038", "TJK100039", "TJK100040", "TJK100044", "TJK100047", "TJK100048", "TJK100049", "TJK100050", "TJK100051", "TJK100052", "TJK100055", "TJK100056", "TJK100059", "TJK100060", "TJK100062", "TJK100063", "TJK100064", "TJK100065", "TJK100066", "TJK100001", "TJK100002", "TJK100003", "TJK100004", "TJK100005", "TJK100006", "TJK100007", "TJK100008", "TJK100009", "TJK100010", "TJK100011", "TJK100018", "TJK100019", "TJK100020", "TJK100021", "TJK100022", "TJK100026", "TJK100027", "TJK100028", "TJK100031", "TJK100032", "TJK100033", "TJK100041", "TJK100042", "TJK100043", "TJK100046", "TJK100053", "TJK100054", "TJK100057", "TJK100058", "TJK100061", "TJK100067"])
GCPIDArr = np.array (["79158", "79159", "79160", "79161", "79162", "79163", "79164", "79165", "79166", "79167", "79168", "79169", "79170", "79171", "79172", "79173", "79174", "79175", "79176", "79177", "79178", "79179", "79180", "79181", "79182", "79183", "79184", "79185", "79186", "79187", "79188", "79189", "79190", "79191", "79192", "79193", "79194", "79195", "79196", "79197", "79198", "79199", "79200", "79201", "79202", "79203", "79204", "79205", "79206", "79207", "79208", "79209", "79210", "79211", "79212", "79213", "79214", "79215", "79216", "79217", "79218", "79219", "79220", "79221", "79222", "79223", "79224", "79225", "79226", "79227", "79228", "79229", "79230", "79231", "79232", "79233", "79234", "79235", "79236", "79237", "79238", "79239", "79240", "79241", "79242", "79243", "79244", "79245", "79246", "79247", "79248", "79249", "79250", "79251", "79252", "79253", "79254", "79255", "79256", "79257", "79258", "79259", "79260", "79261", "79262", "79263", "79264", "79265", "79266", "79267", "79268", "79269", "79270", "79271", "79272", "79273", "79274", "79275", "79276", "79277", "79278", "79279", "79280", "79281", "79282", "79283", "79284", "79285", "79286", "79287", "79288", "79289", "79290", "79291", "79292", "79293", "79294", "79295", "79296", "79297", "79298", "79299", "79300", "79301", "79302", "79303", "79304", "79305", "79306", "79307", "79308", "79309", "79310", "79311", "79312", "79313", "79314", "79315", "79316", "79317", "79318", "79319", "79320", "79321", "79322", "79323", "79324", "79325", "79326", "79327", "79328", "79329", "79330", "79331", "79332", "79333", "79334", "79335", "79336", "79337", "79338", "79339", "79340", "79341", "79377", "79378", "79379", "79380", "79381", "79382", "79383", "79384", "79385", "79386", "79387", "79388", "79389", "79390", "79391", "79392", "79393", "79394", "79395", "79396", "79397", "79398", "79399", "79400", "79401", "79402", "79403", "79404", "79405", "79406", "79407", "79408", "79409", "79410", "79411", "79412", "79413", "79414", "79415", "79416", "79417", "79418", "79419", "79420", "79421", "79422", "79423", "79424", "79425", "79426", "79427", "79342", "79343", "79344", "79345", "79346", "79347", "79348", "79349", "79350", "79351", "79352", "79353", "79354", "79355", "79356", "79357", "79358", "79359", "79360", "79361", "79362", "79363", "79364", "79365", "79366", "79367", "79368", "79369", "79370", "79371", "79372", "79373", "79374", "79375", "79376", "79428", "79429", "79430", "79431", "79432", "79433", "79434", "79435", "79436", "79437", "79438", "79439", "79440", "79441", "79442", "79443", "79444", "79445", "79446", "79447", "79448", "79449", "79450", "79451", "79452", "79453", "79454", "79455", "79456", "79457", "79458", "79459"])
print(dstPath)
for i in range (0, len(PIDArr)):
    print(PIDArr[i])
    PIDNameCU   = PIDArr[i] + "_CU.jpg"
    GCPIDNameCU = GCPIDArr[i] + "_CU.jpg"
    PIDNameE   = PIDArr[i] + "_E.jpg"
    GCPIDNameE = GCPIDArr[i] + "_E.jpg"
    PIDNameN   = PIDArr[i] + "_N.jpg"
    GCPIDNameN = GCPIDArr[i] + "_N.jpg"
    PIDNameS   = PIDArr[i] + "_S.jpg"
    GCPIDNameS = GCPIDArr[i] + "_S.jpg"
    PIDNameW   = PIDArr[i] + "_W.jpg"
    GCPIDNameW = GCPIDArr[i] + "_W.jpg"

    srcFile = os.path.join(srcPath, PIDNameCU)
    dstFile = os.path.join(dstPath, GCPIDNameCU)
    shutil.copy(srcFile, dstFile)

    srcFile = os.path.join(srcPath, PIDNameE)
    dstFile = os.path.join(dstPath, GCPIDNameE)
    shutil.copy(srcFile, dstFile)

    srcFile = os.path.join(srcPath, PIDNameN)
    dstFile = os.path.join(dstPath, GCPIDNameN)
    shutil.copy(srcFile, dstFile)

    srcFile = os.path.join(srcPath, PIDNameS)
    dstFile = os.path.join(dstPath, GCPIDNameS)
    shutil.copy(srcFile, dstFile)

    srcFile = os.path.join(srcPath, PIDNameW)
    dstFile = os.path.join(dstPath, GCPIDNameW)
    shutil.copy(srcFile, dstFile)


