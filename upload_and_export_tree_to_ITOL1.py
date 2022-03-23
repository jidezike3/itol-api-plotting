import argparse
from itolapi import Itol, ItolExport
import os

parser = argparse.ArgumentParser(description='Upload tree to ITOL')

parser.add_argument('-path_to_tree', type=str, help='path to tree file')
parser.add_argument('-APIkey', type=str, help='API key for you personal ITOL account')
parser.add_argument('-ProjectName', type=str, help='Specific Project name to upload tree to.')
parser.add_argument('-treeName',type=str, required=False)
parser.add_argument('-colorbar', type=str, required=False)
parser.add_argument('-path_output_image_tree', type=str, required=False)
parser.add_argument('-include_leaf_labels',type=int)

args = parser.parse_args()
#print(args.accumulate(args.integers))


print(args.APIkey)
print(args.treeName)

#def upload_tree_to_itol(path_to_tree_file,APIkey,ProjectName):
itol_uploader = Itol()
itol_uploader.add_file(args.path_to_tree)
if args.colorbar!=None:
	itol_uploader.add_file(args.colorbar)
	#number of files added to ITOL server for upload (newick file & colorbar annotation)
	num_files=2
else:
	num_files=1

itol_uploader.params["APIkey"] =args.APIkey
itol_uploader.params["projectName"] =args.ProjectName

        #start working here:
if args.treeName==None:
	itol_uploader.params["treeName"] = args.path_to_tree.split('/')[-1].split('.')[0]
else:
	itol_uploader.params["treeName"]=args.treeName
good_upload = itol_uploader.upload()
if good_upload!=False:
	print("SUCCESS!")
	website=itol_uploader.get_webpage()
	print("Website to Tree: "+website)
else:
	print("Unable to Upload Tree!")

        #website=itol_uploader.get_webpage()
        #print("Website to Tree:
#if args.colorbar!=None:
#itol_uploader.add_file(args.colorbar)
	
tree_id = itol_uploader.comm.tree_id
itol_exporter = ItolExport()
itol_exporter.set_export_param_value("tree", tree_id)
itol_exporter.set_export_param_value("tree", tree_id)
file_format='png'
itol_exporter.set_export_param_value("format", file_format)
itol_exporter.set_export_param_value("format", 'png')
itol_exporter.set_export_param_value("display_mode", 2)
itol_exporter.set_export_param_value("arc", 359)
itol_exporter.set_export_param_value("rotation", 270)
itol_exporter.set_export_param_value("leaf_sorting", 1)
#label for leaves?
itol_exporter.set_export_param_value("label_display",int(args.include_leaf_labels))
itol_exporter.set_export_param_value("internal_marks", 0)
use_branch_lengths=False
itol_exporter.set_export_param_value("ignore_branch_length", 1 - int(use_branch_lengths))

#num_files=2
itol_exporter.set_export_param_value("datasets_visible", ",".join([str(i) for i in range(num_files)]))
itol_exporter.set_export_param_value("horizontal_scale_factor", 1)
#itol_exporter.set_export_param_value("tree_x", 2)
#itol_exporter.set_export_param_value("label_display",1)
#itol_exporter.export('/home/jezike/testing_itol_api.png')

if args.path_output_image_tree!=None:
	itol_exporter.export(args.path_output_image_tree)
else:
	itol_exporter.export(os.getcwd()+'/test_tree.png')
#upload_tree_to_itol(args.path_to_tree,args.APIkey,args.ProjectName)
