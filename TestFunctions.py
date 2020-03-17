import pandas
import json
import xlrd


def create_database_dict(db_details_list, json_file_dict):
    for db_detail in db_details_list:
        if db_detail.Index == 0:
            json_file_dict["DatabaseName"] = db_detail.DatabaseName
            json_file_dict["SchemaName"] = db_detail.SchemaName

    return json_file_dict


def add_filter_and_final_columns(list_row, table1_where_details, table2_where_details, column_details):
    if list_row.Table1FilterColumnsColumn != "":
        table1_where_dict = {}
        table1_where_dict["Column"] = list_row.Table1FilterColumnsColumn
        table1_where_dict["Operator"] = list_row.Table1FilterColumnsOperator
        table1_where_dict["Value"] = list_row.Table1FilterColumnsValue
        table1_where_details.append(table1_where_dict.copy())

    if list_row.Table2FilterColumnsColumn != "":
        table2_where_dict = {}
        table2_where_dict["Column"] = list_row.Table2FilterColumnsColumn
        table2_where_dict["Operator"] = list_row.Table2FilterColumnsOperator
        table2_where_dict["Value"] = list_row.Table2FilterColumnsValue
        table2_where_details.append(table2_where_dict.copy())

    if list_row.ColumnsColumnName != "":
        column_where_dict = {}
        column_where_dict["Name"] = list_row.ColumnsColumnName
        column_where_dict["Datatype"] = list_row.ColumnsDatatype
        column_where_dict["AliasName"] = list_row.ColumnsAliasName
        column_details.append(column_where_dict.copy())


def create_queries_list(queries_list):
    previous_transform = ""
    json_entries = []
    json_entry = {}

    table1_details = {}
    table1_where_details = []

    table2_details = {}
    table2_where_details = []

    column_details = []
    for list_row in queries_list:
        if list_row.Index not in (0, 1):
            current_transform = list_row.TransformationName
            if previous_transform != current_transform:
                table1_details["WhereConditions"] = table1_where_details
                table2_details["WhereConditions"] = table2_where_details

                json_entry["Table1"] = table1_details
                json_entry["Table2"] = table2_details
                json_entry["FinalColumns"] = column_details

                # print(json_entry)
                json_entries.append(json_entry.copy())

                json_entry = {}
                table1_details = {}
                table2_details = {}
                table1_where_details = []
                table2_where_details = []
                column_details = []

                json_entry["Query"] = list_row.Query
                json_entry["FinalTable"] = list_row.FinalTable
                json_entry["FinalTableName"] = list_row.FinalTableName
                json_entry["WriteFormat"] = list_row.WriteFormat

                table1_details["TableName"] = list_row.Table1TableName
                table1_details["Format"] = list_row.Table1Format
                table1_details["S3Retrieval"] = list_row.Table1S3Retrieval

                table2_details["TableName"] = list_row.Table2TableName
                table2_details["Format"] = list_row.Table2Format
                table2_details["S3Retrieval"] = list_row.Table2S3Retrieval

            add_filter_and_final_columns(list_row, table1_where_details, table2_where_details, column_details)
            previous_transform = current_transform

    json_entries.append(json_entry.copy())
    json_entries.pop(0)
    return json_entries

queries_df = pandas.read_excel("Test_Json.xlsx", sheet_name="Queries").fillna("")
db_details_df = pandas.read_excel("Test_Json.xlsx", sheet_name="Database_Details").fillna("")
# created_json = df.to_json(orient="records")

#using spark




queries_list = queries_df.itertuples()
db_details_list = db_details_df.itertuples()
json_file_dict = {}
json_file_dict["Queries"] = create_queries_list(queries_list)
json_file_dict = create_database_dict(db_details_list, json_file_dict)

with open('outputfile.json', 'w') as fout:
    json.dump(json_file_dict, fout)
