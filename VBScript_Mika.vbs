'================================
'撰寫者：Mika
'撰寫日期：2022/08-2022/11
'自動化測試工具：Micro focus UFT
'使用語言：VBScript
'主要用途：模擬輸入資料方式、查詢、輸出資料
'================================



'=============
'用途：查詢結果，並新增結果
'抓取頁面上標題，使用多個屬性來確保抓取的標題正確。
'=============

'_查詢結果明細
DataTable("_頁次") = Browser("系統").Page("系統").WebEdit("結果_頁次").Object.value

'_新增查詢結果 Sheet
QuerySheetName = DataTable("No", dtGlobalSheet) & "_結果"
DataTable.AddSheet(QuerySheetName).AddParameter "勾選", ""

'_找尋標題物件
Set titleDesc = Description.Create()
titleDesc("micclass").value = "WebElement"
titleDesc("class").value = "pt-table-head"
titleDesc("class").RegularExpression = True
titleDesc("visible").value = True
titleDesc("html tag").value = "DIV"
Set titleObj = Browser("micclass:=Browser").Page("micclass:=Page").ChildObjects(titleDesc)

'_查詢結果標題
For i = 1 To titleObj.Count -1
    titleStr = titleObj(i).GetROProperty("outertext")
    DataTable.GetSheet(QuerySheetName).AddParameter titleStr, ""
    If titleStr = "交易事件時間" Then Exit for
Next


'=============
'用途：找尋 checkbox物件並且勾選。
'條件：限制10筆。
'根據DataTable中的資料對比頁面上的查詢結果。
'勾選對應的資料，勾選上限為10筆，以防超過系統限制。
'=============

'_找尋checkbox物件
Set checkDesc = Description.Create()
checkDesc("micclass").value = "WebCheckBox"
checkDesc("visible").value = True
checkDesc("name").value = "dataitemindex"
checkDesc("type").value = "checkbox"
Set checkObj = Browser("micclass:=Browser").Page("micclass:=Page").ChildObjects(checkDesc)

checkCount = 0
TargetCustomer = DataTable("用戶名稱", dtGlobalSheet)

For i = 1 To DataTable.GetSheet(QuerySheetName).GetRowCount
    DataTable.GetSheet(QuerySheetName).SetCurrentRow i

    '_當 detailStr = DataTable 的用戶名稱 時，就勾選。
    If instr(DataTable("用戶名稱", QuerySheetName), TargetCustomer) And TargetCustomer <> "" Then
        checkObj(i-1).FireEvent "OnFocus"
        checkObj(i-1).Set "On"
        wait 1
        DataTable("勾選", QuerySheetName) = "v"
        checkCount = checkCount + 1
    End if

    '_超過系統限制10筆，就跳出迴圈。
    If checkCount = 10 Then Exit for
Next


'=============
'用途：使用迴圈查詢結果，並達到條件後換行，讓輸出內容格式統一。
'=============

'_查詢結果標題 (0000 查詢結果)
For i = 1 To titleObj.Count -1
    titleStr = titleObj(i).GetROProperty("outertext")
    DataTable.GetSheet(QuerySheetName).AddParameter titleStr, ""
    If titleStr = "交易事件時間" Then Exit for
Next

'_查詢結果內容
nextDetailCol = 1  '_同一行下一個欄位 (第 x 個欄位)
nextRowCount = 1  '_換行用
For i = 0 To detailObj.Count -1
    detailStr = detailObj(i).GetROProperty("outertext")

    '_當 detailStr = DataTable 的位置行 時，就換行。
    If detailStr <> DataTable("位置行", dtGlobalSheet) Then
        If detailStr <> "" Then
            DataTable.GetSheet(QuerySheetName).GetParameter(nextDetailCol).Value = "'" & detailStr
        End If
        nextDetailCol = nextDetailCol + 1
    Else
        DataTable.GetSheet(QuerySheetName).GetParameter(nextDetailCol).Value = "'" & detailStr
        nextRowCount = nextRowCount + 1
        DataTable.GetSheet(QuerySheetName).SetCurrentRow nextRowCount
        nextDetailCol = 1
    End If
Next
