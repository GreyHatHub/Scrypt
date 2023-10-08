import subprocess

class VPNCommand:

    def DefaultIPTABLES(self):
        subprocess.call(["./proxyDefault.sh"])
        
        print("\n####################")            
        print("Set Default Setting")
        print("####################")  
		
    def iptables_OVpn(self):
        subprocess.call(["./proxyOVPN.sh"])
		
        print("\n####################")            
        print("Set OpenVPN setting")
        print("####################") 
	
    def main(self):
		
        countvpn=input("\n[0. Default setting]\n[1. OpenVPN setting]\n\n[Enter number setting, default 0]: ")
        if countvpn.__len__()==0 or countvpn=='0':
            self.DefaultIPTABLES()
        else:
            self.iptables_OVpn()

if __name__ == '__main__':
    parser = VPNCommand()
    parser.main()