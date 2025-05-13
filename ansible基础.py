ansible hosts定义：
	[default]  #组名
	172.0.0.11  ansible_ssh_user=root ansible_ssh_pass=""
	
主入口 yml
	---
	- name: xx
	  hosts: default
	  vars:
	    user: sam
	  gather_facts: False    #获取被控机器的fact数据，默认开启，你需要设置 gather_facts: False来关闭
	  roles:
	    - only_archiving

playbook调用方式: ansible-playbook -i hosts only_archiving.yaml

变量定义：
	1. 主入口yaml中定义
	2. group_vars/default/default.yaml                     #群组变量定义，组名同hosts组名
	3. roles/role_name/{vars,defaults}/main.yaml           #ROLE变量定义, role下的vars目录和defaults目录都可以进行变量定义
	
roles
	rolename1:
		defaults          #存放默认的变量，模板文件中的变量就是引用自这里
			main.yml
		vars              #同defaults，可定义变量
		files             #存放文件
		templates         #存放模板文件。template模块会将模板文件中的变量替换为实际值
			nginx.conf.j2
		tasks
			main.yaml
				---
				- name: xx
				  shell: 
				  ignore_errors: True
				  register: war_name
				
				- name: xx
				  shell: "for i in `ls xx`;do xx;done"
				  args:
				    chdir: xx
				  when: service_name.stdout == "servicename"
				  
				- name: xx                       #循环模块with_items
				  shell: "{{ item }}"
				  with_items:
				    - "echo {{ 1 }}"
					- "echo {{ 2 }}"
					
				- name: xx
				  copy:
				    src: eureka                  #eureka目录可定义在role_name/files/下
					dest: xx
					mode: 0755
					
				- name: xx
					template:
					  src: xx.j2
					  dest:
					  mode: 0755
					  
				- name:
				  fail:                         #失败判断、类似return False
				    msg:
				  when: install_status|failed  #is defined, is not defined
	rolename2:

遗留：
    ansible copy和template区别？
