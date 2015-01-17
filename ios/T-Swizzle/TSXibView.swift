//
//  TSXibView.swift
//  T-Swizzle
//
//  Created by Benjamin Y Chan on 1/17/15.
//  MIT License
//  Concept borrowed from Paul Solt (2014)
//  ======================================
//
//  Inheriting from this allows you to init views based on a xib, and treat
//  them as an object that can be inserted into other Xib files, or what not
//

import UIKit

class TSXibView: UIView {
    
    var _customView: UIView?
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        // load the xib file, which must share the same name as view file
        let className: String = NSStringFromClass(self.dynamicType).componentsSeparatedByString(".").last!
        _customView = NSBundle.mainBundle().loadNibNamed(className, owner: self, options: nil).first as? UIView
        
        // modify our bounds
        if (CGRectIsEmpty(frame)) {
            self.bounds = _customView!.bounds
        }
        
        // add as real subview
        self.addSubview(_customView!)
    }

    required init(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        
        // load the xib file, which must share the same name as view file
        // hackish way to parse a class name.
        let className: String = NSStringFromClass(self.dynamicType).componentsSeparatedByString(".").last!
        _customView = NSBundle.mainBundle().loadNibNamed(className, owner: self, options: nil).first as? UIView
        
        // add it as a real subview
        self.addSubview(_customView!)
    }

    

}
