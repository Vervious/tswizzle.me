//
//  ViewController.swift
//  T-Swizzle
//
//  Created by Jennifer Zhang on 1/17/15.
//  Copyright (c) 2015 tswizzle. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController, FBLoginViewDelegate {
    
    @IBOutlet var fbLoginView : FBLoginView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.fbLoginView.delegate = self;
        self.fbLoginView.readPermissions = ["public_profile", "email", "user_friends", "publish_stream"]
        
        self.view.backgroundColor = UIColor(red: 192.0, green: 57.0, blue: 43.0, alpha: 1.0)
        
    }
    
    //FACEBOOK DELEGATE METHODS
    
    //If the user is already logged in
    
    func loginViewShowingLoggedInUser(loginView : FBLoginView!) {
        NSLog("User Logged In")
        
        self.performSegueWithIdentifier("toTheSwizzle", sender: self)
        
    }
    
    func loginViewFetchedUserInfo(loginView : FBLoginView!, user: FBGraphUser){
        NSLog("User Name: \(user.name)")
    }
    
    //If the user is logged out
    
    func loginViewShowingLoggedOutUser(loginView : FBLoginView!) {
        NSLog("User Logged Out")
    }
    
    //Errors
    
    func loginView(loginView : FBLoginView!, handleError:NSError) {
        NSLog("Error: \(handleError.localizedDescription)")
    }
    
    
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}

