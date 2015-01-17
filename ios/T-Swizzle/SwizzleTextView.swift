//
//  SwizzleTextView.swift
//  T-Swizzle
//
//  Created by Benjamin Y Chan on 1/17/15.
//  Copyright (c) 2015 tswizzle. All rights reserved.
//

import UIKit

// Instantiate only from a xib file. Else,
// override all the init methods because config is currently
// set in awakeFromNib for simplicity.
class SwizzleTextView: UITextView {

    override func awakeFromNib() {
        // text attributes
        textColor = UIColor.whiteColor()
        font = UIFont(name: "HelveticaNeue-Bold", size: 50.0)
        
        // layout
        textContainerInset = UIEdgeInsetsMake(30, 30, 30, 60)
        
        // background setup
        backgroundColor = UIColor.blackColor()
    }
}
