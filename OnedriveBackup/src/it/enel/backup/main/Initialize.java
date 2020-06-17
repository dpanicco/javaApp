package it.enel.backup.main;

import java.io.File;

public class Initialize {

	static File homeDirectory = new File(System.getProperty("user.home") + "\\.OnedriveBackup");
	static String homeDrive = System.getenv("HOMEDRIVE");
	static String fileSep = System.getProperty("file.separator");
	
	public static boolean isInitialized() {
		
		if (!homeDirectory.exists())
			return initialize();
		else
			if (homeDirectory.isDirectory())
				return readInit();
		
		return false;
	}
	
	public static boolean initialize() {
		
		
		return false;
	}
	
	public static boolean readInit() {
		
		
		return false;
	}
}
